import requests
import time
from typing import Dict, Optional, Union, Any
from .utils import get_default_logger
from .schema import DatasetDict


class HttpClient:
    MAX_RETRIES: int = 4

    @classmethod
    def get(
        cls,
        url: str,
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, str]] = None,
        logger=None,
        stream: Optional[bool] = False,
    ):
        """
        General get request function.
        Assigns headers and builds in retries and logging
        :param url: str: api host, example: https://www.example.com/api?x=1
        :param headers: Dict[str, str]: headers
        :param params: Dict[str, str]: params
        :param logger: Logger: logger
        :param stream: bool:
        """
        """General 'make api request' function.
      Assigns headers and builds in retries and logging.
      """
        base_log_record: Dict[str, Union[str, Dict[str, str]]] = dict(
            route=url, params=params
        )
        retry_count: int = 0

        if not logger:
            logger = get_default_logger()
            logger.debug(url)
            logger.debug(params)
        while retry_count <= cls.MAX_RETRIES:
            start_time: float = time.time()
            try:
                response = requests.get(
                    url, params=params, headers=headers, timeout=None, stream=stream
                )
            except Exception as e:
                response = e

            elapsed_time: float = time.time() - start_time
            status_code: int = (
                response.status_code if hasattr(response, "status_code") else None
            )
            log_record: Dict[str, Union[int, float, str, Dict[str, str]]] = dict(
                base_log_record
            )
            log_record["elapsed_time_in_ms"] = 1000 * elapsed_time
            log_record["retry_count"] = retry_count
            log_record["status_code"] = status_code
            if status_code == 200:  # Success
                logger.debug("OK", extra=log_record)
                return response
            if status_code in [204, 206]:  # Success with a caveat - warning
                log_msg = {204: "No Content", 206: "Partial Content"}[status_code]
                logger.warning(log_msg, extra=log_record)
                return response
            log_record["tag"] = "failed_gro_api_request"
            if retry_count < cls.MAX_RETRIES:
                logger.warning(
                    response.text if hasattr(response, "text") else response,
                    extra=log_record,
                )
            if status_code in [400, 401, 402, 404, 301]:
                break  # Do not retry
            logger.warning("{}".format(response), extra=log_record)
            if retry_count > 0:
                # Retry immediately on first failure.
                # Exponential backoff before retrying repeatedly failing requests.
                time.sleep(2**retry_count)
            retry_count += 1
        raise APIError(response, retry_count, url)

    @classmethod
    def post(
        cls,
        url: str,
        data: Optional[DatasetDict] = None,
        json=None,
        headers: Optional[Dict[str, str]] = None,
        files: Optional[Dict] = None,
        logger=None,
        stream: Optional[bool] = False,
    ):
        """
        General post request function.
        Assigns headers and builds in retries and logging
        :param url: str: api host, example: https://www.example.com/api?x=1
        :param headers: Dict[str, str]: headers
        :param data: Dict[str, str]: params
        :param json: json data
        :param files: files
        :param logger: Logger: logger
        :param stream: bool:
        """
        """General 'make api request' function.
     Assigns headers and builds in retries and logging.
     """
        base_log_record: Dict = dict(route=url, data=data)
        retry_count: int = 0
        if not logger:
            logger = get_default_logger()
            logger.debug(url)
            logger.debug(data)
        while retry_count <= cls.MAX_RETRIES:
            start_time: float = time.time()
            try:
                if data:
                    response = requests.post(
                        url,
                        data=data,
                        headers=headers,
                        files=files,
                        timeout=None,
                        stream=stream,
                    )
                else:
                    response = requests.post(
                        url,
                        json=json,
                        headers=headers,
                        files=files,
                        timeout=None,
                        stream=stream,
                    )
            except Exception as e:
                response = e

            elapsed_time: float = time.time() - start_time
            status_code: int = (
                response.status_code if hasattr(response, "status_code") else None
            )
            log_record: Dict[str, Union[int, float, str, Dict[str, str]]] = dict(
                base_log_record
            )
            log_record["elapsed_time_in_ms"] = 1000 * elapsed_time
            log_record["retry_count"] = retry_count
            log_record["status_code"] = status_code
            if status_code in [200, 204]:  # Success
                logger.debug("OK", extra=log_record)
                return response
            log_record["tag"] = "failed_gro_api_request"
            if retry_count < cls.MAX_RETRIES:
                logger.warning(
                    response.text if hasattr(response, "text") else response,
                    extra=log_record,
                )
            if status_code in [400, 401, 402, 404, 301]:
                break  # Do not retry
            logger.warning("{}".format(response), extra=log_record)
            if retry_count > 0:
                # Retry immediately on first failure.
                # Exponential backoff before retrying repeatedly failing requests.
                time.sleep(2**retry_count)
            retry_count += 1
        raise APIError(response, retry_count, url)

    @classmethod
    def put(
        cls,
        url: str,
        json: DatasetDict = None,
        data: Union[str, Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        logger=None,
        stream: Optional[bool] = False,
    ):
        """
        General put request function.
        Assigns headers and builds in retries and logging
        :param url: str: api host, example: https://www.example.com/api?x=1
        :param headers: Dict[str, str]: headers
        :param json: json data
        :param data: Dict[str, str]: params
        :param logger: Logger: logger
        :param stream: bool:
        """
        """General 'make api request' function.
      Assigns headers and builds in retries and logging.
      """
        base_log_record: Dict = dict(route=url, data=json)
        retry_count: int = 0
        if not logger:
            logger = get_default_logger()
            logger.debug(url)
            logger.debug(json)
        while retry_count <= cls.MAX_RETRIES:
            start_time: float = time.time()
            try:
                if json:
                    response = requests.put(
                        url, json=json, headers=headers, timeout=None, stream=stream
                    )
                else:
                    response = requests.put(
                        url, data=data, headers=headers, timeout=None, stream=stream
                    )
            except Exception as e:
                response = e

            elapsed_time: float = time.time() - start_time
            status_code: int = (
                response.status_code if hasattr(response, "status_code") else None
            )
            log_record: Dict[str, Union[int, float, str, Dict[str, str]]] = dict(
                base_log_record
            )
            log_record["elapsed_time_in_ms"] = 1000 * elapsed_time
            log_record["retry_count"] = retry_count
            log_record["status_code"] = status_code
            if status_code == 200:  # Success
                logger.debug("OK", extra=log_record)
                return response
            log_record["tag"] = "failed_gro_api_request"
            if retry_count < cls.MAX_RETRIES:
                logger.warning(
                    response.text if hasattr(response, "text") else response,
                    extra=log_record,
                )
            if status_code in [400, 401, 402, 404, 301]:
                break  # Do not retry
            logger.warning("{}".format(response), extra=log_record)
            if retry_count > 0:
                # Retry immediately on first failure.
                # Exponential backoff before retrying repeatedly failing requests.
                time.sleep(2**retry_count)
            retry_count += 1
        raise APIError(response, retry_count, url)


class APIError(Exception):
    def __init__(
        self,
        response,
        retry_count: int,
        url: str,
    ):
        self.response = response
        self.retry_count: int = retry_count
        self.url: str = url
        self.status_code = (
            response.status_code if hasattr(response, "status_code") else None
        )
        try:
            json_content = self.response.json()
            # 'error' should be something like 'Not Found' or 'Bad Request'
            self.message: str = json_content.get("error", "")
            # Some error responses give additional info.
            # For example, a 400 Bad Request might say "metricId is required"
            if "message" in json_content:
                self.message += ": {}".format(json_content["message"])
        except (Exception,):
            # If the error message can't be parsed, fall back to a generic "giving up" message.
            self.message = "Giving up on {} after {} {}: {}".format(
                self.url,
                self.retry_count,
                "retry" if self.retry_count == 1 else "retries",
                response,
            )
