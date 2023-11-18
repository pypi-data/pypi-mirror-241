import os
from .version import Version
from .StorageManager import StorageManager
from .schema import (
    FileEntryDict,
    ApiRequestArgs,
    EntityListInstances,
    DatasetDict,
    DatasetState,
    FileEntries,
)
from copy import deepcopy
from enum import Enum
import tqdm
from typing import Optional, List, Dict, Union, Set, Tuple
from typeguard import typechecked
from pathlib import Path
from .utils import (
    sha256sum,
    matches_any_wildcard,
)
from multiprocessing.pool import ThreadPool
import psutil
import uuid
from copy import copy
from .ServerFacade import ServerFacade
from .utils import (
    check_env_variables,
)
from concurrent.futures import ThreadPoolExecutor, wait, as_completed, ALL_COMPLETED
from .ParallelZipper import ParallelZipper
from zipfile import ZIP_DEFLATED
import shutil
from time import time
from .logger import Logger

logger = Logger().get_logger()


class FileEntry(object):
    """
    This class aids in the retrieval and upload of files associated with a dataset.
    It allows us to determine if a file has been successfully uploaded to cloud the storage, identifies
    the parent dataset to which the file belongs, and provides essential details for downloading the file.
    """

    def __init__(
        self,
        relative_path: str,
        parent_dataset_id: str,
        artifact_name: Optional[str] = None,
        local_path: Optional[str] = None,
        size: Optional[int] = None,
        hash_: Optional[str] = None,
        remote_url_basename: Optional[str] = None,
    ) -> None:
        """
        Initialize a FileEntry object.

        :param relative_path: str: The relative path of the file within the dataset.
        :param parent_dataset_id: str: The unique identifier of the parent dataset.
            the dataset that the file belongs
        :param artifact_name: str: The name of the artifact that the file belongs.
            All files with the same parent dataset will be stored in chunks of the same size
            and each chunk corresponds to an artifact. The naming of artifacts follows a sequential pattern
            with the first artifact named "data," and subsequent artifacts named "data_1," "data_2," and so on.
        :param local_path: str: The local file path.
        :param size: int: The size of the file in bytes.
        :param hash_: str: The hash value of the file.
            We use it to check whether the file has been modified or  not
        :param remote_url_basename: str: The basename of the remote URL.
            In general, when we upload files to cloud storage the remote base URL serves
            as the file's name on the cloud storage platform.
        """
        self.artifact_name = artifact_name
        self.relative_path = relative_path
        self.parent_dataset_id = parent_dataset_id
        self.size = size
        self.hash = hash_
        # cleared when file is uploaded.
        self.local_path = local_path
        # added when we upload the file
        self.remote_url_basename = remote_url_basename

    def serializer(self) -> FileEntryDict:
        """
        Serializes the object data into dict
        :return: dict:
        """
        state: FileEntryDict = {
            "artifact_name": self.artifact_name,
            "relative_path": self.relative_path,
            "hash": self.hash,
            "parent_dataset_id": self.parent_dataset_id,
            "size": self.size,
        }
        state["remote_url_basename"] = (
            self.remote_url_basename if self.remote_url_basename else None
        )
        state["local_path"] = self.local_path if self.local_path else None
        return state


class DatasetStatusEnum(Enum):
    def __str__(self) -> str:
        return str(self.value)

    def __eq__(self, other) -> bool:
        return str(self) == str(other)

    created: str = "created"
    in_progress: str = "in_progress"
    uploaded: str = "uploaded"
    failed: str = "failed"
    completed: str = "completed"
    aborted: str = "aborted"


STATUS_FLOW = {
    DatasetStatusEnum.created.value: [
        DatasetStatusEnum.in_progress.value,
        DatasetStatusEnum.completed.value,
        DatasetStatusEnum.aborted.value,
        DatasetStatusEnum.failed.value,
    ],
    DatasetStatusEnum.in_progress.value: [
        DatasetStatusEnum.uploaded.value,
        DatasetStatusEnum.aborted.value,
        DatasetStatusEnum.failed.value,
    ],
    DatasetStatusEnum.uploaded.value: [
        DatasetStatusEnum.completed.value,
        DatasetStatusEnum.in_progress.value,
        DatasetStatusEnum.aborted.value,
        DatasetStatusEnum.failed.value,
    ],
}


class DatasetClient(object):
    """
    The core class of the ML dataset client that provides a comprehensive set of methods
    to effectively manage datasets. These methods include functions for adding and removing
    files, uploading and downloading data, and finalizing dataset operations.
    This class serves as the central interface for interacting with machine learning datasets
    """

    __dataset_entity_name: str = "ml_dataset"
    __workspace_entity_name: str = "workspace"
    __default_dataset_version: str = "1.0.0"
    # The cloud storage directory name where the datasets will be stored.
    __datasets_entry_name: str = "datasets"
    # The name of teh cloud storage directory that will hold the state file.
    # A state file contains information about all the file entries within the dataset.
    # example state-> state.json
    __state_entry_name: str = "state"
    # The cloud storage parent directory of __datasets_entry_name example: data->datasets
    __default_data_entry_name: str = "data"
    # we us it as a prefix when naming artifacts example data_1,data_2....
    __data_entry_name_prefix: str = "data_"
    # Artifact chunk size (MB) for the compressed dataset.
    _dataset_chunk_size_mb: int = 512
    __dataset_platform: str = "oip"
    # The local directory name where the datasets will be stored.
    __dataset_download_folder_context: str = "datasets"
    # The directory prefix for storing downloaded dataset files.
    # It always follows the format 'prefix_{UUID of the dataset}'.
    __dataset_download_folder_prefix: str = "ds"

    @classmethod
    @typechecked
    def connect(cls, api_host: str, api_key: str, workspace_name: str) -> None:
        """
        Connect to the remote MLDataset platform
        It will check if the workspace exists and get its id
        Then set the the api host, the workspace id, the workspace_name, and the api key
        :param api_host: str: The API Host
        :param api_key: str: The API Key
        :param workspace_name: str: The workspace name
        :return: none:
        """

        os.environ["OIP_API_HOST"] = api_host
        os.environ["DATASET_AUTHENTICATION_TOKEN"] = api_key

        # Check if workspace exists
        api_request_args: ApiRequestArgs = {
            "filter_cols": "name",
            "filter_ops": "=",
            "filter_vals": workspace_name,
        }

        data = ServerFacade.get_data(
            entity=cls.__workspace_entity_name,
            api_request_args=api_request_args,
        )
        if not data:
            raise ValueError(f"WORKSPACE {workspace_name} DOES NOT EXIST")

        # Get workspace id
        workspace_id: str = data[0]["id"]
        os.environ["DATASET_WORKSPACE_NAME"] = workspace_name
        os.environ["WORKSPACE_ID"] = workspace_id

    @typechecked
    def __init__(
        self,
        name: str,
        id_: str = None,
        workspace_id: Optional[str] = None,
        version: Optional[str] = None,
        is_main: bool = False,
        parent_datasets: List[str] = None,
        status: Optional[str] = None,
        file_count: int = 0,
        added_files: int = 0,
        modified_files: int = 0,
        removed_files: int = 0,
        total_size: int = 0,
        total_size_compressed: Optional[int] = 0,
        description: str = None,
        tags: List[str] = None,
    ):
        """
        Create a new dataset, Do not use directly! Use Dataset.create(...).
        :param name: str: Naming the new dataset.
        :param id_: str: Id of the new Dataset.
        :param workspace_id: str: The workspace ID to which the new dataset will belong.
        :param version: str: Version of the new dataset. If not set, try to find the latest version
            of the dataset with given `name`  and auto-increment it.
        :param is_main: bool: True if this version is the main version
        :param parent_datasets: list[str]: List of parent datasets (parent ids)
        :param status: str: Status of the new-dataset
            status in [created,in_progress,uploaded,completed,aborted,failed,unknown]
        :param file_count: int: The total count of files within the dataset.
        :param added_files: int: The total count of files added to the dataset
            Added files refer to those that are not part of the direct or indirect
            parent datasets of the new dataset.
        :param modified_files: int: The total count of files modified within the dataset.
            Modified files are files that belong to the direct or indirect parent datasets
            and we upload a modified version of these files to the new dataset.
        :param removed_files: int: The total count of files removed from the new dataset.
            Removed files are files that belong to the direct or indirect parent datasets
            ,and we have removed them from the new dataset.
        :param total_size: int: The total size of all the files within the new dataset
            including both the direct and indirect parent files.
        :param total_size_compressed: int: The total compressed size of all the files within the new dataset
            including both the direct and indirect parent files.
        :param description: str: Description of the dataset
        :param tags: list[str]: Descriptive tags categorize datasets by keywords, detailing their subject
            matter, domain, or specific topics for better identification and organization.
        :return: Newly created Dataset object
        """

        self._name = name
        self._id: str = id_ if id_ else str(uuid.uuid4())
        self._status: str = DatasetStatusEnum.created.value if not status else status
        self._version: str = version
        self._is_main = is_main
        if not parent_datasets:
            parent_datasets = []
        self._parent_datasets = parent_datasets
        self._workspace_id: str = workspace_id or os.environ["WORKSPACE_ID"]

        self._description: str = description
        if not tags:
            tags = []
        self._tags = tags
        self._file_count: int = file_count
        self._added_files: int = added_files
        self._modified_files: int = modified_files
        self._removed_files: int = removed_files
        self._total_size: int = total_size
        self._total_size_compressed: int = total_size_compressed

        self._file_entries: Dict[str, FileEntry] = {}
        self._dependency_graph: Dict[str, List[str]] = {}
        # set current artifact name to be used (support for multiple upload sessions)
        self._data_artifact_name: str = self._get_next_data_artifact_name()
        # store a cached lookup of the number of chunks each parent dataset has.
        self._dependency_chunk_lookup: Optional[Dict[str, int]] = None

    @property
    def id(self) -> str:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def version(self) -> str:
        return self._version

    @property
    def is_main(self) -> bool:
        return self._is_main

    @property
    def parent_datasets(self) -> List[str]:
        return self._parent_datasets

    @property
    def tags(self) -> List[str]:
        return self._tags

    @property
    def workspace_id(self) -> str:
        return self._workspace_id

    @version.setter
    @typechecked
    def version(self, version: str) -> None:
        """
        Version Setter
        :param version: str:
        :return: str:
        """
        version = str(version).strip()

        if not Version.is_valid_version_string(version):
            raise ValueError(f"{version} is not a valid version")
        else:
            self._version = version

    @property
    def total_size(self) -> int:
        return self._total_size

    @property
    def total_size_compressed(self) -> int:
        return self._total_size_compressed

    @property
    def file_entries(self) -> List[FileEntry]:
        return list(self._file_entries.values())

    @property
    def file_count(self) -> int:
        return self._file_count

    @property
    def added_files(self) -> int:
        return self._added_files

    @property
    def modified_files(self) -> int:
        return self._modified_files

    @property
    def removed_files(self) -> int:
        return self._removed_files

    @property
    def file_entries_dict(self) -> Dict[str, FileEntry]:
        """
        File entries ad dict
        :return: dict with relative file path as key, and FileEntry as value
        """
        return self._file_entries

    @typechecked
    def _update_status(self, new_status: str) -> None:
        """
        Update Dataset status
        :param new_status: str: new status
        :return: none
        """
        if new_status not in STATUS_FLOW[self._status]:
            raise ValueError(f"forbidden flow  form {self._status} to {new_status}")
        self._status = new_status

    @typechecked
    def _get_next_data_artifact_name(
        self, last_data_artifact_name: Optional[str] = None
    ) -> str:
        """
        Get the next data artifact name
        :param last_data_artifact_name: str: name of the last data artifact example data_x
        :return: str:the next data artifact name example data_x+1
        """
        if not last_data_artifact_name:
            # the default value of the first data artifact
            return self.__default_data_entry_name
        else:
            prefix: str = self.__data_entry_name_prefix
            last_artificat_version: int = (
                int(last_data_artifact_name[len(prefix):])
                if last_data_artifact_name.startswith(prefix)
                else 0
            )

        return f"{prefix}{last_artificat_version+1:03d}"

    @classmethod
    @typechecked
    def create(
        cls,
        name: str,
        parent_datasets: List[str] = None,
        version: str = None,
        is_main: bool = False,
        description: str = None,
        tags: List[str] = None,
    ):
        """
        Create a new dataset
        :param name: str: Naming the new dataset.
        :param version: str: version of the new dataset. If not set, try to find the latest version
        :param parent_datasets: list[str]: A list of parent datasets to extend the new dataset
            by adding all the files from their respective parent datasets
        :param is_main: boolean: True if this is the main dataset
        :param description: str: Description of the dataset
        :param parent_datasets: list[str]: Descriptive tags categorize datasets by keywords, detailing their
            subject matter, domain, or specific topics for better identification and organization.
        :param tags: List[str]: List of tags to be associated with the datset
        :return: Newly created Dataset object
        """
        logger.debug("call dataset create")

        if name == "":
            raise ValueError("`dataset name` can't be an empty string")

        if not parent_datasets:
            parent_datasets = list()

        parent_datasets_ = [
            cls.get(dataset_id=p_id) for p_id in (parent_datasets or [])
        ]
        if any(not p.is_completed() for p in parent_datasets_):
            raise ValueError(
                "can't inherit from a parent that was not finalized/closed"
            )
        if version:
            version = str(version).strip()
            if not Version.is_valid_version_string(version):
                raise ValueError(f"{version} is not a valid version")
        if not tags:
            tags = []

        dataset = cls(
            name=name,
            version=version,
            is_main=is_main,
            parent_datasets=parent_datasets,
            description=description,
            tags=tags,
        )
        # make sure that the first version is always the main one
        if not is_main and dataset._is_first_version():
            dataset._is_main = True

        if not dataset._version:
            latest_version: str = dataset._get_highest_version()
            if latest_version is not None:
                dataset._version = str(Version(latest_version).get_next_version())
            else:
                dataset._version = cls.__default_dataset_version
        # merge datasets according to order
        dependency_graph: Dict[str, List[str]] = {}
        parent_file_entries: Dict[str, FileEntry] = {}
        total_size: int = 0
        for p in parent_datasets_:
            parent_file_entries.update(deepcopy(p._file_entries))
            dependency_graph.update(deepcopy(p._dependency_graph))
            total_size += p.total_size

        # key for the dataset file entries are the relative path within the data
        dataset._file_entries = parent_file_entries
        dataset._file_count = len(dataset.file_entries)
        dataset._total_size = total_size
        # this will create a graph of all the dependencies we have, each entry lists it's own direct parents
        dataset._dependency_graph = dependency_graph
        dataset._dependency_graph[dataset._id] = [p._id for p in parent_datasets_]
        dataset._update_dependency_graph()
        data: DatasetDict = dataset.serializer()
        # Fields that are excluded from being stored on the server.
        excluded_fields: List[str] = [
            "dependency_graph",
            "file_entries",
            "dependency_chunk_lookup",
        ]
        for field in excluded_fields:
            data.pop(field)
        # Upload the state file to the cloud storage.
        dataset._upload_state()
        # Store the data on the sever
        cls._save(method="create", data=data)
        logger.info("THE DATASET HAS BEEN SUCCESSFULLY CREATED")
        return dataset

    def _get_highest_version(self) -> Union[str, None]:
        """
        Get the highest semantic version of the dataset
        :return: str: the last version of the dataset
        """
        check_env_variables()

        workspace_id: str = os.environ["WORKSPACE_ID"]

        api_request_args: ApiRequestArgs = {
            "filter_cols": f"name|{self.__workspace_entity_name}_id",
            "filter_ops": "=|=",
            "filter_vals": f"{self.name}|{workspace_id}",
            "sort_col": "version",
            "sort_order": "-1",
        }
        data: EntityListInstances = ServerFacade.get_data(
            entity=self.__dataset_entity_name,
            api_request_args=api_request_args,
        )
        return data[0]["version"] if data else None

    def _is_first_version(self) -> bool:
        """
        Check if the current version is the first version
        :return: bool: true if the current version is the first version of the dataset
        """
        check_env_variables()

        workspace_id: str = os.environ["WORKSPACE_ID"]

        api_request_args: ApiRequestArgs = {
            "filter_cols": f"name|{self.__workspace_entity_name}_id",
            "filter_ops": "=|=",
            "filter_vals": f"{self.name}|{workspace_id}",
        }
        data: EntityListInstances = ServerFacade.get_data(
            entity=self.__dataset_entity_name,
            api_request_args=api_request_args,
        )
        return len(data) == 0

    @classmethod
    @typechecked
    def get(
        cls,
        dataset_id: Optional[str] = None,
        dataset_name: Optional[str] = None,
        dataset_version: Optional[str] = None,
        only_completed: Optional[bool] = False,
        auto_create: Optional[bool] = False,
    ):
        """
        Get a specific Dataset. If multiple datasets are found, the dataset with the
        highest semantic version is returned. This functions raises an Exception in case no dataset
        can be found and the ``auto_create=True`` flag is not set

        :param dataset_id: str: Requested dataset ID
        :param dataset_name: str: Requested dataset name
        :param dataset_version: str: Requested version of the Dataset
        :param only_completed: str: Return only if the requested dataset is completed
        :param auto_create: bool: Create a new dataset if it does not exist yet
        :return: Dataset object
        """

        if not any([dataset_id, dataset_name]):
            raise ValueError(
                "Dataset selection criteria not met. Didn't provide id/name correctly."
            )

        if dataset_id:
            api_request_args: ApiRequestArgs = {
                "filter_cols": "id",
                "filter_ops": "=",
                "filter_vals": f"{dataset_id}",
                "sort_col": "version",
                "sort_order": "-1",
            }
        else:
            check_env_variables()
            workspace_id: str = os.environ["WORKSPACE_ID"]
            if not dataset_version:
                api_request_args = {
                    "filter_cols": "name|workspace_id",
                    "filter_ops": "=|=",
                    "filter_vals": f"{dataset_name}|{workspace_id}",
                    "sort_col": "version",
                    "sort_order": "-1",
                }

            else:
                api_request_args = {
                    "filter_cols": "name|workspace_id|version",
                    "filter_ops": "=|=|=",
                    "filter_vals": f"{dataset_name}|{workspace_id}|{dataset_version}",
                }
        if only_completed:
            api_request_args["filter_cols"] += "|status"
            api_request_args["filter_ops"] += "|="
            api_request_args["filter_vals"] += "|completed"

        data: EntityListInstances = ServerFacade.get_data(
            entity=cls.__dataset_entity_name,
            api_request_args=api_request_args,
        )
        if data:
            # return the latest version
            dataset = cls._deserializer([data[0]])[0]
            return dataset
        elif not data and auto_create and dataset_name:
            dataset = cls.create(name=dataset_name, version=dataset_version)
            return dataset
        else:
            raise ValueError(
                f"Could not find Dataset {'id' if dataset_id else 'name/version'} "
                f"{dataset_id if dataset_id else (dataset_name, dataset_version)}"
            )

    @typechecked
    def get_local_copy(self, max_workers: Optional[int] = None) -> None:
        """
        Get a local copy of the entire dataset
        :param max_workers: int: Number of threads to be spawned when getting the dataset copy.
            Defaults to the number of logical cores.
        :return: None
        """
        if not self.is_completed():
            raise ValueError(
                "can't get a local copy of a dataset that was not finalized"
            )
        max_workers = max_workers or psutil.cpu_count()
        target_base_folder: str = self._create_ds_target_base_folder()
        artifacts: Dict[str, List[Dict]] = self._get_artifacts_to_download()
        # we download into temp_local_path so if we accidentally stop in the middle,
        # we won't think we have the entire dataset
        timestamp = str(time()).replace(".", "")
        temp_target_base_folder = f"{target_base_folder}_{timestamp}_partially"
        os.rename(target_base_folder, temp_target_base_folder)
        with ThreadPoolExecutor(max_workers=max_workers) as pool:
            if self._id in artifacts:
                self._get_dataset_files_from_artifacts(
                    artifacts[self.id], temp_target_base_folder, pool
                )
            self._merge_parent_datasets(artifacts, temp_target_base_folder, pool)
        os.rename(temp_target_base_folder, target_base_folder)

    @typechecked
    def _get_dataset_files_from_artifacts(
        self, artifacts: List[Dict], target_folder: str, pool=None
    ) -> str:
        """
        Retrieve all dataset files from a specific artifacts, which means obtaining all
        the files associated with a particular chunks.
        :param artifacts: list[Dict]: list of artifacts names
            example :[{artifact_name:"..",remote_url_basename:".."},..{..}]
        :param target_folder: str: path of the  Target folder for the download files
        :param pool:ThreadPool: A thread pool for concurrent execution of tasks.
        :return: str: path to the target folder
        """
        download_features: List = []
        unzip_features: List = []
        downloads: List = []
        for art in artifacts:
            remote_url: str = self.generate_object_name(
                dataset_name=self._name,
                dataset_id=self._id,
                artifact_name=art["artifact_name"],
                file_path=art["remote_url_basename"],
            )
            for download_task in download_features[:]:
                if download_task.done():
                    unzip_features.append(
                        pool.submit(
                            shutil.unpack_archive, download_task.result(), target_folder
                        )
                    )
                    download_features.remove(download_task)

            download_path: str = os.path.join(target_folder, art["remote_url_basename"])
            downloads.append(download_path)
            download_features.append(
                pool.submit(StorageManager.download, remote_url, download_path)
            )
        for download_task in as_completed(download_features):
            unzip_features.append(
                pool.submit(
                    shutil.unpack_archive, download_task.result(), target_folder
                )
            )

        completed_unzip, not_completed_unzip = wait(
            unzip_features, return_when=ALL_COMPLETED
        )
        for download_path in downloads:
            pool.submit(os.remove, download_path)
        for unzip_task in completed_unzip:
            if unzip_task.exception() is not None:
                raise Exception(
                    f"unpack_archive raised an exception: {unzip_task.exception()}"
                )
        # update target folder timestamp
        Path(target_folder).touch()

        return target_folder

    @typechecked
    def _merge_parent_datasets(
        self, artifacts: Dict[str, List[Dict]], target_base_folder: str, pool
    ) -> None:
        """
        Download files from the parent datasets and place them within the same target folder
        :param artifacts: dict[str,list[str]]: artifacts for the dataset and all its parents
               example {dataset_id: list_of_direct_artifacts,...}
        :param target_base_folder: str: path of the base target folder for the download files
        :param pool:ThreadPool: A thread pool for concurrent execution of tasks.
        :return: none
        """
        for parent_id in artifacts.keys():
            if parent_id == self._id:
                continue
            ds_parent = self.get(parent_id)
            parent_target_folder: str = self._create_ds_target_base_folder()
            ds_parent._get_dataset_files_from_artifacts(
                artifacts[parent_id], parent_target_folder, pool
            )

            @typechecked
            def copy_file(file_entry) -> Optional[Exception]:
                """
                Copy a file form the parent source folder to the final target folder
                :param file_entry:FileEntry: file entry example: {relative_path:"",size:,..}
                :return: none
                """
                if file_entry.parent_dataset_id == parent_id:
                    source: str = (
                        Path(parent_target_folder) / Path(file_entry.relative_path)
                    ).as_posix()
                    target: str = (
                        Path(target_base_folder) / Path(file_entry.relative_path)
                    ).as_posix()
                    try:
                        shutil.copy2(source, target)
                    except Exception as ex:
                        return ex

                    return None
                return None

            errors: List = pool.map(copy_file, self._file_entries.values())

            if any(errors):
                raise Exception(
                    "Dataset merging failed: {}".format(
                        [e for e in errors if e is not None]
                    )
                )
            shutil.rmtree(parent_target_folder)

    def _create_ds_target_base_folder(self) -> str:
        """
        Create a target base folder for storing the downloaded dataset files
        :return: str: path of the target folder

        """
        target_base_folder: str = os.path.join(
            self.__dataset_platform,
            self.__dataset_download_folder_context,
            self._name,
            f"{self.__dataset_download_folder_prefix}_{self._id}",
        )
        target_folder: str = target_base_folder
        suffix: int = 1
        # check if the folder already exist if yes we add a suffix
        while os.path.exists(target_folder):
            target_folder = f"{target_base_folder}-{str(suffix)}"
            suffix += 1
        Path(target_folder).mkdir(parents=True)
        return target_folder

    def _get_parents(self) -> List[str]:
        """
        Return a list of direct parent datasets (str)
        :return: list[str]: list of dataset ids
        """
        return self._dependency_graph[self.id]

    @classmethod
    @typechecked
    def _deserializer(cls, data: EntityListInstances):
        """
        Deserialize a list of dictionaries into a list of dataset objects.
        :param data:EntityListInstances:
        :return: list: return a list dataset objects

        """
        datasets: List = []
        for d in data:
            for key in copy(d):
                if key.startswith("_"):
                    del d[key]
                elif key in [
                    "file_count",
                    "added_files",
                    "removed_files",
                    "modified_files",
                    "total_size",
                    "total_size_compressed",
                ]:
                    # cast float to int
                    # when we get the data from the server we get is as float
                    d[key] = int(d[key])
            dataset = cls(**d)
            dataset_state: DatasetState = dataset._download_state()
            dataset._dependency_graph = dataset_state["dependency_graph"]
            dataset._dependency_chunk_lookup = dataset_state["dependency_chunk_lookup"]
            for f in dataset_state["file_entries"]:
                dataset._file_entries[f["relative_path"]] = FileEntry(**f)
            datasets.append(dataset)

        return datasets

    @typechecked
    def _add_files(
        self,
        path: str,
        wildcard: Optional[Union[str, List[str]]] = None,
        local_base_folder: Union[str, Path] = None,
        dataset_path: Optional[str] = None,
        recursive: Optional[bool] = True,
        max_workers: Optional[int] = None,
    ) -> Tuple[int, int]:
        """
        Add files to the dataset.
         To add files to the dataset, we follow these steps:
           1-Calculate the file hash.
           2-Compare it against the parent dataset.
           3-If the file doesn't exist or has been modified, add it to the list of files to be uploaded later.
        :param path: str: path to the files we want to add to our dataset
        :param wildcard: str: add only specific set of files.
            Wildcard matching, can be a single string or a list of wildcards
        :param local_base_folder: str: files will be located based on their relative path from local_base_folder
        :param dataset_path: str: where in the dataset the folder/files should be located
        :param recursive: bool: If True, match all wildcard files recursively
        :param max_workers: int: The number of threads to add the files with. Defaults to the number of logical cores
        :return: tuple[int,int]: return (added_files,modified_files)
        """
        max_workers = max_workers or psutil.cpu_count()
        if dataset_path:
            dataset_path = dataset_path.lstrip("/")
        path_: Path = Path(path)
        local_base_folder = Path(local_base_folder or path)
        wildcard = wildcard or ["*"]
        if isinstance(wildcard, str):
            wildcard = [wildcard]
        # single file, no need for threading
        if path_.is_file():
            if not local_base_folder.is_dir():
                local_base_folder = local_base_folder.parent
            file_entry = self._calc_file_hash(
                FileEntry(
                    local_path=path_.absolute().as_posix(),
                    relative_path=(
                        Path(dataset_path or ".") / path_.relative_to(local_base_folder)
                    ).as_posix(),
                    parent_dataset_id=self._id,
                )
            )
            file_entries: List = [file_entry]
        else:
            # if not a folder raise exception
            if not path_.is_dir():
                raise ValueError(f"Could not find file/folder { path_.as_posix()}")

            # prepare a list of files
            file_entries = []
            for w in wildcard:
                files: List[Path] = (
                    list(path_.rglob(w)) if recursive else list(path_.glob(w))
                )
                file_entries.extend([f for f in files if f.is_file()])
            file_entries = list(set(file_entries))
            file_entries = [
                FileEntry(
                    parent_dataset_id=self._id,
                    local_path=f.absolute().as_posix(),
                    relative_path=(
                        Path(dataset_path or ".") / f.relative_to(local_base_folder)
                    ).as_posix(),
                )
                for f in file_entries
            ]

            pool = ThreadPool(max_workers)
            try:
                # Displaying progress bars when calculating file hashes
                for _ in tqdm.tqdm(
                    pool.imap_unordered(self._calc_file_hash, file_entries),
                    total=len(file_entries),
                ):
                    pass
            except ImportError:
                pool.map(self._calc_file_hash, file_entries)
            pool.close()

        # merge back into the dataset
        added_files: int = 0
        modified_files: int = 0
        for f in file_entries:
            ds_cur_f: FileEntry = self._file_entries.get(f.relative_path)
            if not ds_cur_f:
                self._file_entries[f.relative_path] = f
                added_files += 1
            elif ds_cur_f.hash != f.hash:
                self._file_entries[f.relative_path] = f
                modified_files += 1
            elif (
                f.parent_dataset_id == self._id
                and ds_cur_f.parent_dataset_id == self._id
            ):
                # check if we have the file in an already uploaded chunk
                if ds_cur_f.local_path:
                    self._file_entries[f.relative_path] = f
                    added_files += 1
        if added_files or modified_files:
            self._update_status(new_status=DatasetStatusEnum.in_progress.value)
        return added_files, modified_files

    @typechecked
    def add_files(
        self,
        path: str,
        wildcard: Optional[Union[str, List[str]]] = None,
        local_base_folder: str = None,
        dataset_path: Optional[str] = None,
        recursive: Optional[bool] = True,
        max_workers: Optional[int] = None,
    ) -> Tuple[int, int]:
        """
        Add files to the dataset.
         To add files to the dataset, we follow these steps:
           1-Calculate the file hash.
           2-Compare it against the parent dataset.
           3-If the file doesn't exist or has been modified, add it to the list of files to be uploaded later.
        :param path: str: path to the files we want to add to our dataset
        :param wildcard: str: add only specific set of files.
            Wildcard matching, can be a single string or a list of wildcards
        :param local_base_folder: str: files will be located based on their relative path from local_base_folder
        :param dataset_path: str: where in the dataset the folder/files should be located
        :param recursive: bool: If True, match all wildcard files recursively
        :param max_workers: int: The number of threads to add the files with. Defaults to the number of logical cores
        :return: tuple[int,int]: return (added_files,modified_files)
        """
        if self.is_final():
            raise Exception(
                "Files can't be added to a dataset that has already been finalized."
            )
        logger.debug("call add_files")
        logger.info("ADDING FILES ...")
        max_workers = max_workers or psutil.cpu_count()
        added_files, modified_files = self._add_files(
            path=path,
            wildcard=wildcard,
            local_base_folder=local_base_folder,
            dataset_path=dataset_path,
            recursive=recursive,
            max_workers=max_workers,
        )

        self._update_file_entries_post_processing(removed_operation=False)
        data_to_be_updated: DatasetDict = {
            "id": self._id,
            "added_files": self._added_files,
            "removed_files": self._removed_files,
            "modified_files": self._modified_files,
            "total_size": self.total_size,
            "total_size_compressed": self.total_size_compressed,
            "file_count": self.file_count,
        }
        self._upload_state()
        self._save(method="update", data=data_to_be_updated)
        logger.info("FILES ADDED SUCCESSFULLY")
        return added_files, modified_files

    @typechecked
    def remove_files(self, dataset_path: str, recursive: Optional[bool] = True) -> int:
        """
        Remove files from the current dataset
        :param dataset_path: str: path to the files to remove.
            The path is always relative to the dataset (e.g 'folder/file.bin').
        :param recursive: bool: If True, match all wildcard files recursively
        :return: int: Number of files removed
        """

        if self.is_final():
            raise Exception(
                "Files can't be removed from a dataset that has already been finalized."
            )
        logger.info("REMOVING FILES ...")
        if dataset_path and dataset_path.startswith("/"):
            dataset_path = dataset_path[1:]
        self._file_entries = {
            relative_path: v
            for relative_path, v in self._file_entries.items()
            if not matches_any_wildcard(
                relative_path, dataset_path, recursive=recursive
            )
        }
        self._update_file_entries_post_processing()
        data_to_be_updated: DatasetDict = {
            "id": self._id,
            "removed_files": self._removed_files,
            "added_files": self._added_files,
            "modified_files": self._modified_files,
            "total_size": self.total_size,
            "total_size_compressed": self.total_size_compressed,
            "file_count": self.file_count,
        }
        self._upload_state()
        self._save(method="update", data=data_to_be_updated)
        logger.info("FILES REMOVED SUCCESSFULLY")
        return self.removed_files

    @typechecked
    def _update_file_entries_post_processing(
        self, removed_operation: Optional[bool] = True
    ) -> None:
        """
        Update dataset state
           the dataset's state changes every time we call add_files or remove_files
        :param removed_operation: bool: In case post-processing is triggered following a removal operation.
        """
        self._update_dependency_graph()
        self._file_count = len(self.file_entries)

        parent_file_entries: FileEntries = self._get_parent_file_entries()
        added_files: int = 0
        modified_files: int = 0
        total_size: int = 0

        for file in self._file_entries.values():
            total_size += file.size
            if file.parent_dataset_id == self._id:
                if file.relative_path in parent_file_entries:
                    modified_files += 1
                else:
                    added_files += 1

        self._added_files = added_files
        self._modified_files = modified_files
        self._total_size = total_size
        if removed_operation:
            removed_files: int = 0
            for parent_entry_key, parent_entry_value in parent_file_entries.items():
                if parent_entry_key not in self._file_entries:
                    removed_files += 1
            self._removed_files = removed_files

    def _build_dependency_chunk_lookup(self) -> Dict[str, int]:
        """
        Build the dependency dataset id to number-of-chunks
        :return: dict[str,int] lookup dictionary from dataset-id to number of chunks
        """
        chunks_lookup: map = map(
            lambda dataset_id: (
                dataset_id,
                (
                    self if dataset_id == self.id else DatasetClient.get(dataset_id)
                )._get_num_chunks(),
            ),
            self._dependency_graph.keys(),
        )
        return dict(chunks_lookup)

    def _get_num_chunks(self) -> int:
        """
        Return the number of chunks stored on this dataset
           it does not imply on the number of chunks parent versions store
        :return: int: Number of chunks stored on the dataset.
        """
        artifacts: List[str] = self._get_data_artifact_names()

        return len(artifacts)

    def _get_data_artifact_names(self) -> List[str]:
        """
        Get all the artifact names in the dataset including parent artifacts
        :return: list[str]: return all the artifact names
        """
        artifacts: List[str] = []
        for file in self.file_entries:
            if (
                file.parent_dataset_id == self.id
                and file.artifact_name not in artifacts
            ):
                artifacts.append(file.artifact_name)

        return artifacts

    def _get_artifacts_to_download(self) -> Dict[str, List[Dict]]:
        """
        Get the necessary information to download all files in the dataset and its parent datasets.
            we need artifact_name and remote_url_basename(file name in the could storage)
        :return: dict[str,list[dict]] example
            {dataset_id:[{artifact_name:"..",remote_url_basename:".."},..]},
            {parent_1_id:[]},
            ...}}
        """
        artifacts: Dict[str, List] = {}
        for file in self.file_entries:
            if (
                file.parent_dataset_id in artifacts
                and file.artifact_name not in artifacts[file.parent_dataset_id]
            ):
                artifacts[file.parent_dataset_id].append(
                    {
                        "artifact_name": file.artifact_name,
                        "remote_url_basename": file.remote_url_basename,
                    }
                )
            elif file.parent_dataset_id not in artifacts:
                artifacts[file.parent_dataset_id] = [
                    {
                        "artifact_name": file.artifact_name,
                        "remote_url_basename": file.remote_url_basename,
                    }
                ]

        return artifacts

    def _get_parent_file_entries(self) -> FileEntries:
        """
        Get parent file entries
        :return: dict[str,file_entry]: example
            {parent_1_id:parent_1_file_entries},
            ...}}
        """
        parent_datasets_ids: List[str] = self._dependency_graph[self._id]
        parent_file_entries: FileEntries = dict()
        for parent_dataset_id in parent_datasets_ids:
            parent_dataset = self.get(parent_dataset_id)
            parent_file_entries.update(parent_dataset._file_entries)

        return parent_file_entries

    def _update_dependency_graph(self) -> None:
        """
        Update the dependency graph based on the current self._file_entries state
        :return: none
        """
        # collect all dataset versions
        used_dataset_versions: Set = set(
            f.parent_dataset_id for f in self._file_entries.values()
        )
        used_dataset_versions.add(self._id)
        current_parents: List = self._dependency_graph.get(self._id) or []
        # remove parent versions we no longer need from the main version list
        # per version, remove unnecessary parent versions, if we do not need them
        self._dependency_graph = {
            k: [p for p in parents or [] if p in used_dataset_versions]
            for k, parents in self._dependency_graph.items()
            if k in used_dataset_versions
        }
        # make sure we do not remove our parents
        self._dependency_graph[self._id] = current_parents

    @typechecked
    def _upload_state(self) -> None:
        """
        Upload the state of the dataset to the cloud storage service.
        """
        state: DatasetState = dict(
            file_count=self._file_count,
            total_size=self._total_size,
            file_entries=[f.serializer() for f in self._file_entries.values()],
            dependency_graph=self._dependency_graph,
            dependency_chunk_lookup=self._dependency_chunk_lookup,
            id=self._id,
        )
        object_name: str = self.generate_state_object_name(self._name, self._id)
        StorageManager.upload_state(object_name=object_name, dataset_state=state)

    def _download_state(self) -> DatasetState:
        """
        Download the state of the dataset to the cloud storage service.
        :return: DatasetState: a dict that represent the sate of the dataset.
        """
        object_name: str = self.generate_state_object_name(self._name, self._id)
        state: DatasetState = StorageManager.download_state(object_name)
        return state

    @typechecked
    def upload(
        self,
        compression: Optional[int] = None,
        chunk_size: Optional[int] = None,
        max_workers: Optional[int] = None,
    ) -> None:
        """
        Start file uploading, the function returns when all files are uploaded.

        :param compression: int: Compression algorithm for the Zipped dataset file (default: ZIP_DEFLATED)
        :param chunk_size: int: Artifact chunk size (MB) for the compressed dataset,
            if not provided (None) use the default chunk size (512mb).
        :param max_workers: int:Numbers of threads to be spawned when zipping and uploading the files.
            If None number of logical cores
        :return: none
        """
        if self.is_final():
            raise Exception(
                "Files can't be uploaded as the dataset has already been finalized."
            )
        logger.info("UPLOADING FILES ...")
        if not max_workers:
            max_workers = psutil.cpu_count()

        total_size: int = 0
        chunks_count: int = 0
        keep_as_file_entry: Set = set()
        chunk_size = int(self._dataset_chunk_size_mb if not chunk_size else chunk_size)
        upload_tasks: List = []

        with ThreadPoolExecutor(max_workers=max_workers) as pool:
            parallel_zipper = ParallelZipper(
                chunk_size,
                max_workers,
                allow_zip_64=True,
                compression=ZIP_DEFLATED if compression is None else compression,
                zip_prefix="dataset.{}.".format(self._id),
                zip_suffix=".zip",
                pool=pool,
            )
            file_paths: List[str] = []
            zip_names: Dict[str, str] = {}
            for f in self._file_entries.values():
                if not f.local_path:
                    keep_as_file_entry.add(f.relative_path)
                    continue
                file_paths.append(f.local_path)
                zip_names[f.local_path] = f.relative_path
            for zip_ in parallel_zipper.zip_iter(file_paths, zip_names):
                running_tasks: List = []
                for upload_future in upload_tasks:
                    if upload_future.running():
                        running_tasks.append(upload_future)
                    else:
                        if not upload_future.result():
                            raise Exception(
                                "Failed uploading dataset with ID {}".format(self._id)
                            )
                upload_tasks = running_tasks

                artifact_name: str = self._data_artifact_name
                self._data_artifact_name = self._get_next_data_artifact_name(
                    self._data_artifact_name
                )
                total_size += zip_.size
                zip_path: Path = Path(zip_.zip_path)
                zip_file_name: str = os.path.basename(zip_path)
                object_name: str = self.generate_object_name(
                    self._name, self._id, artifact_name, zip_file_name
                )
                upload_tasks.append(
                    pool.submit(
                        StorageManager.upload,
                        object_name=object_name,
                        path=zip_.zip_path,
                    )
                )
                chunks_count += 1
                for file_entry in self._file_entries.values():
                    if (
                        file_entry.local_path is not None
                        and Path(file_entry.local_path).as_posix() in zip_.files_zipped
                    ):
                        keep_as_file_entry.add(file_entry.relative_path)
                        file_entry.artifact_name = artifact_name
                        file_entry.remote_url_basename = zip_file_name
                        if file_entry.parent_dataset_id == self._id:
                            file_entry.local_path = None
                self._upload_state()
        self._update_status(new_status=DatasetStatusEnum.uploaded.value)

        if chunks_count == 0:
            # No pending files, skipping upload
            data_to_be_updated: DatasetDict = {"id": self._id, "status": self._status}
            self._save("update", data_to_be_updated)

        # remove files that could not be zipped
        self._file_entries = {
            k: v
            for k, v in self._file_entries.items()
            if v.relative_path in keep_as_file_entry
        }
        self._update_file_entries_post_processing()
        data_to_be_updated = {
            "id": self._id,
            "added_files": self._added_files,
            "removed_files": self._removed_files,
            "modified_files": self._modified_files,
            "total_size": self.total_size,
            "total_size_compressed": self.total_size_compressed,
            "file_count": self.file_count,
            "status": self._status,
        }
        self._save("update", data_to_be_updated)
        self._upload_state()
        logger.info("FILES UPLOADED SUCCESSFULLY")

    @typechecked
    def finalize(self, auto_upload=False) -> None:
        """
        Finalize the dataset. Upload must first be called to verify that there are no pending uploads.
        If files do need to be uploaded, it throws an exception.
        :param auto_upload: bool: Automatically upload dataset if not called yet, will upload to default location.
        """
        # check we do not have files waiting for upload.
        if self._status == DatasetStatusEnum.in_progress.value:
            if auto_upload:
                self.upload()
            else:
                raise Exception(
                    "can't finalize dataset, pending uploads. Call Dataset.upload(...)"
                )

        if self._status not in (
            DatasetStatusEnum.created.value,
            DatasetStatusEnum.uploaded.value,
        ):
            raise Exception(
                f"can't finalize dataset, status '{self._status}' is not valid"
            )
        self._update_status(new_status=DatasetStatusEnum.completed.value)
        self._dependency_chunk_lookup = self._build_dependency_chunk_lookup()

        self._upload_state()
        data_to_be_updated: DatasetDict = {"id": self._id, "status": self._status}
        self._save("update", data_to_be_updated)
        logger.info("DATASET COMPLETED SUCCESSFULLY")

    @classmethod
    @typechecked
    def generate_object_name(
        cls, dataset_name: str, dataset_id: str, artifact_name: str, file_path: str
    ) -> str:
        """
        Generate object name (object that we need to upload to the cloud storage)
        :param dataset_name: str: name of the dataset
        :param dataset_id: str: id of the dataset
        :param artifact_name:: str: artifact name
        :param file_path: str: file path
        :return: str: object name
        """
        check_env_variables()
        workspace_name: str = os.environ["DATASET_WORKSPACE_NAME"]
        object_name: str = os.path.join(
            cls.__dataset_entity_name,
            workspace_name,
            cls.__datasets_entry_name,
            dataset_name,
            f"{dataset_name}.{dataset_id}",
            artifact_name,
            file_path,
        )
        return object_name

    @classmethod
    @typechecked
    def generate_state_object_name(cls, dataset_name: str, dataset_id: str) -> str:
        """
        Generate state object name (state object that we need to upload to the cloud storage)
        :param dataset_name: str: name of the dataset
        :param dataset_id: str: id of the dataset
        :return: str: state object name
        """
        check_env_variables()
        workspace_name = os.environ["DATASET_WORKSPACE_NAME"]
        object_name = os.path.join(
            cls.__dataset_entity_name,
            workspace_name,
            cls.__datasets_entry_name,
            dataset_name,
            f"{dataset_name}.{dataset_id}",
            cls.__state_entry_name,
            f"{cls.__state_entry_name}.json",
        )
        return object_name

    def serializer(self) -> DatasetDict:
        """
        Serializes the object data into dict
        :return:Dataset: return a dict that represent the dataset
        """

        file_entries: List[FileEntryDict] = [f.serializer() for f in self.file_entries]

        return {
            "id": self.id,
            "name": self._name,
            "status": self._status,
            "version": self._version,
            "is_main": self._is_main,
            "parent_datasets": self._parent_datasets,
            "tags": self._tags,
            "workspace_id": self._workspace_id,
            "description": self._description,
            "file_count": self.file_count,
            "added_files": self._added_files,
            "removed_files": self._removed_files,
            "modified_files": self._modified_files,
            "total_size": self.total_size,
            "total_size_compressed": self.total_size_compressed,
            "file_entries": file_entries,
            "dependency_graph": self._dependency_graph,
            "dependency_chunk_lookup": self._dependency_chunk_lookup,
        }

    def abort(self) -> None:
        """
        Abort a dataset
        :return:none
        """
        if self.is_final():
            raise Exception(
                "You can't abort a dataset that has already been finalized."
            )
        self._update_status(new_status=DatasetStatusEnum.aborted.value)
        data_to_be_updated: DatasetDict = {"id": self._id, "status": self._status}
        self._upload_state()
        self._save(method="update", data=data_to_be_updated)
        logger.info("DATASET ABORTED SUCCESSFULLY")

    @classmethod
    @typechecked
    def _save(cls, method: str, data: DatasetDict) -> None:
        """
        Save the dataset on the server
        :param method: str: "Create" a new dataset if it doesn't exist, or "update" an existing one .
        :param data: dict: Data we need to create or update.
        :return: none
        """
        ServerFacade.save_data(
            entity=cls.__dataset_entity_name, method=method, data=data
        )

    @staticmethod
    @typechecked
    def _calc_file_hash(file_entry: FileEntry):
        """
        Calculate file hash and add it to the file entry
        :param file_entry:FileEntry:
        :return: FineEntry
        """
        file_entry.hash, _ = sha256sum(file_entry.local_path)
        file_entry.size = Path(file_entry.local_path).stat().st_size
        return file_entry

    def is_completed(self) -> bool:
        """
        Return True if the dataset was completed and can't be changed any more.
        :return: bool: True if dataset is completed correctly
        """
        return self._status == DatasetStatusEnum.completed

    def is_final(self) -> bool:
        """
        Return True if the dataset was finalized and can't be changed any more.
        :return: bool: True if the dataset has reached a final status, which can be one of the following:
            completed, aborted, or failed
        """
        return self._status in [
            DatasetStatusEnum.completed.value,
            DatasetStatusEnum.aborted.value,
            DatasetStatusEnum.failed.value,
        ]
