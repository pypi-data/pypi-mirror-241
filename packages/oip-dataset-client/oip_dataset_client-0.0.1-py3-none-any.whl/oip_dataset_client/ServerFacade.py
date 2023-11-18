import os
from typing import Dict, Optional, Union
from .utils import check_env_variables
from .HttpClient import HttpClient
from .schema import (
    EntityListInstances,
    DatasetDict,
)
from app.modules.dataset.definitions import MODULE_NAME


class ServerFacade:
    @staticmethod
    def save_data(entity: str, method: str, data: DatasetDict):
        """
        Save the data on the server
        :param entity: str: Name of the entity.
        :param method: str: "Create" a new record if it doesn't exist, or "update" an existing record.
        :param data: DatasetDict: Data we need to create or update.
        :return: response content
        """
        if method not in ["create", "update"]:
            raise ValueError(f"METHOD {method} IS NOT ALLOWED")
        check_env_variables()
        api_host: str = os.environ["OIP_API_HOST"]
        base_url: str = os.path.join(api_host, MODULE_NAME, entity)
        base_url = base_url.replace("\\", "/")
        access_token: str = os.environ["DATASET_AUTHENTICATION_TOKEN"]
        headers: Dict = {"authorization": "APIKey " + access_token}
        if method == "create":
            url: str = os.path.join(base_url, "add")
            response = HttpClient.post(url=url, json=data, headers=headers)
        elif method == "update":
            url = os.path.join(base_url, "update")
            response = HttpClient.put(url=url, json=data, headers=headers)

        if response.status_code == 200:
            return response.json()

    @staticmethod
    def get_data(
        entity: str,
        api_request_args: Dict[str, str],
    ) -> Optional[EntityListInstances]:
        """
        Retrieve data from the API based on the provided parameters.

        :param entity: str: The name of the entity for which to retrieve the data.
        :param api_request_args:api_request_args: Additional parameters for the API request.
        :return: list: The retrieved data.
        """
        api_host: str = os.environ["OIP_API_HOST"]
        access_token: str = os.environ["DATASET_AUTHENTICATION_TOKEN"]
        url: str = os.path.join(api_host, MODULE_NAME, entity)
        url = url.replace("\\", "/")
        headers: Dict[str, str] = {"authorization": "APIKey " + access_token}
        resp = HttpClient.get(url, headers, api_request_args)
        if resp.status_code == 200:
            return resp.json()["data"]
        return None

    @staticmethod
    def create_presigned_url(
        object_name: str, is_post_url: Optional[bool] = False
    ) -> Union[str, Dict[str, Union[str, Dict[str, str]]]]:
        """
        Generate a pre-signed URL for accessing an object in the cloud storage.
        :param object_name: str: The name of the object to create a pre-signed URL for.
        :param is_post_url: bool:Set to True if the URL should be for uploading.
            Defaults to False (downloading).
        :return:union[dict,str]: information about the presigned url
        """
        api_host: str = os.environ["OIP_API_HOST"]
        url: str = os.path.join(api_host, MODULE_NAME)
        if is_post_url:
            url = os.path.join(url, "presigned_post_url")
        else:
            url = os.path.join(url, "presigned_get_url")
        url = url.replace("\\", "/")
        access_token: str = os.environ["DATASET_AUTHENTICATION_TOKEN"]
        headers: Dict = {"authorization": "APIKey " + access_token}
        data: Dict = {"object_name": object_name}
        resp = HttpClient.post(url=url, json=data, headers=headers)
        if resp.status_code == 200:
            return resp.json()
        return None
