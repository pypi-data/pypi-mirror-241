from typing import Optional
from .HttpClient import HttpClient
from .ServerFacade import ServerFacade
import tempfile
import json
from pathlib import Path
import os
import requests
from urllib.parse import urlparse
import shutil
from time import time
from .schema import DatasetState

COMPRESSED_EXTENSION = [
    ".zip",
    ".gz",
    ".tar.gz",
    ".bz2",
    ".7z",
    ".rar",
    ".tar",
    ".zst",
    ".xz",
    ".Z",
    ".sit",
    ".sitx",
]


class StorageManager:
    __default_target_folder = "global"
    # in MB
    __chunk_size = 5

    @staticmethod
    def upload_state(object_name: str, dataset_state: DatasetState):
        """
        Upload state file to the cloud storage
        :param object_name: str: object name
        :param dataset_state: DatasetState: dataset state
        """
        presigned_post_data = ServerFacade.create_presigned_url(
            object_name, is_post_url=True
        )
        with tempfile.NamedTemporaryFile(mode="w+") as temp_state_file:
            json.dump(dataset_state, temp_state_file, indent=4)
            temp_state_file.seek(0)
            if presigned_post_data["method"] == "PUT":
                binary_data = temp_state_file.read()
                response = HttpClient.put(
                    **presigned_post_data["kwargs"], data=binary_data
                )
            elif presigned_post_data["method"] == "POST":
                file_ = {"file": (object_name, temp_state_file)}
                response = HttpClient.post(
                    **presigned_post_data["kwargs"],
                    files=file_,
                )

    @staticmethod
    def upload(object_name: str, path: str) -> bool:
        """
        Upload data file to the cloud storage
        :param object_name: str: object name
        :param path: str: path to the file
        :return: bool:
        """
        presigned_post_data = ServerFacade.create_presigned_url(
            object_name, is_post_url=True
        )
        with open(path, "r") as file:
            if presigned_post_data["method"] == "PUT":
                binary_data = file.read()
                response = HttpClient.put(
                    **presigned_post_data["kwargs"], data=binary_data
                )
            else:
                file_ = {"file": (object_name, file)}
                response = HttpClient.post(
                    **presigned_post_data["kwargs"],
                    files=file_,
                )

        return True

    @staticmethod
    def download(object_name: str, download_path: str) -> Optional[str]:
        """
        Download data file from the cloud storage
        :param object_name: str: object name
        :param download_path: str: download location
        :return: bool:
        """
        get_url = ServerFacade.create_presigned_url(object_name)
        response = HttpClient.get(get_url)
        if response.status_code == 200:
            with open(download_path, "wb") as file:
                file.write(response.content)
            return download_path
        return None

    @staticmethod
    def download_state(object_name: str) -> Optional[DatasetState]:
        """
        Download state file from the cloud storage
        :param object_name: str: object name
        :return: DatasetState: dataset state
        """
        get_url = ServerFacade.create_presigned_url(object_name)
        response = HttpClient.get(get_url)
        if response.status_code == 200:
            return response.json()
        return None

    @classmethod
    def get_local_copy(
        cls,
        remote_url: str,
        target_folder: Optional[str] = None,
        extract_archive: Optional[bool] = True,
    ) -> str:
        """
        Get a local copy of a external dataset (dataset that doesn't belong to our storage)
        :param remote_url: str: dataset url
        :type target_folder: str: the local directory where the dataset will be downloaded.
        :param extract_archive: bool: if true extract the compressed file (defaults to True)
        :return: str: path to the downloaded file
        """
        # Parse the URL to extract the path, which includes the filename.
        url_parts = urlparse(remote_url)
        remote_path = url_parts.path
        file_name = remote_path.split("/")[-1]
        if not target_folder:
            target_folder = cls.__default_target_folder
        # we download into temp_local_path so that if we accidentally stop in the middle,
        # we won't think we have the entire file
        timestamp = str(time()).replace(".", "")
        temp_target_folder = f"{target_folder}_{timestamp}_partially"
        temp_dst_file_path = os.path.join(temp_target_folder, file_name)
        Path(temp_target_folder).mkdir(parents=True, exist_ok=True)

        with requests.get(url=remote_url, stream=True) as response:
            try:
                with open(temp_dst_file_path, mode="wb") as file:
                    for chunk in response.iter_content(
                        chunk_size=cls.__chunk_size * 1024
                    ):
                        file.write(chunk)
            except (Exception,):
                shutil.rmtree(temp_target_folder)
                raise Exception("failed in downloading file")

        suffix = Path(temp_dst_file_path).suffix.lower()
        if suffix == ".gz":
            suffix = "".join(a.lower() for a in Path(temp_dst_file_path).suffixes[-2:])
        if extract_archive and suffix in COMPRESSED_EXTENSION:
            try:
                shutil.unpack_archive(temp_dst_file_path, temp_target_folder)
                os.remove(temp_dst_file_path)
                all_folders = os.listdir(temp_target_folder)
                # we expect to find only one folder inside the temporary folder (the unzipped folder)
                unzipped_folder = all_folders[0]
                path_to_unzipped_temp_target_folder = (
                    f"{temp_target_folder}/{unzipped_folder}"
                )
                path_to_unzipped_target_folder = f"{target_folder}/{unzipped_folder}"

                count_suffix = 0
                while os.path.exists(path_to_unzipped_target_folder):
                    count_suffix += 1
                    path_to_unzipped_target_folder = (
                        f"{target_folder}/{unzipped_folder}-{str(count_suffix)}"
                    )
                if count_suffix > 0:
                    os.rename(
                        path_to_unzipped_temp_target_folder,
                        f"{temp_target_folder}/{unzipped_folder}-{count_suffix}",
                    )
                    path_to_unzipped_temp_target_folder = (
                        f"{temp_target_folder}/{unzipped_folder}-{count_suffix}"
                    )
                shutil.move(path_to_unzipped_temp_target_folder, target_folder)
                shutil.rmtree(temp_target_folder)
                return path_to_unzipped_target_folder
            except Exception as e:
                shutil.rmtree(temp_target_folder)
                raise Exception(e)
        else:
            if Path(target_folder).exists():
                count_suffix = 0
                dst_file_path = f"{target_folder}/{file_name}"
                base_file_name = file_name[: -len(suffix)]
                while os.path.exists(dst_file_path):
                    count_suffix += 1
                    dst_file_path = (
                        f"{target_folder}/{base_file_name}-{str(count_suffix)}{suffix}"
                    )

                if count_suffix > 0:
                    os.rename(
                        temp_dst_file_path,
                        f"{temp_target_folder}/{base_file_name}-{count_suffix}{suffix}",
                    )
                    temp_dst_file_path = (
                        f"{temp_target_folder}/{base_file_name}-{count_suffix}{suffix}"
                    )

                shutil.move(temp_dst_file_path, target_folder)
                shutil.rmtree(temp_target_folder)
                return dst_file_path
            else:
                os.rename(temp_target_folder, target_folder)
                return f"{target_folder}/{file_name}"
