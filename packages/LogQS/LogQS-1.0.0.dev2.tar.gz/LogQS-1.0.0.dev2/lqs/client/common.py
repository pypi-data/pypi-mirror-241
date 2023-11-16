from typing import Optional
import requests

import time
import os
import json
import base64
import pprint
import logging
import decimal
from datetime import datetime, date
from uuid import UUID


def get_logger(name, level=None):
    logger = logging.getLogger(name)
    if level is None:
        level = os.getenv("LQS_LOG_LEVEL", "INFO").upper()
    logger.setLevel(level)

    if not logger.handlers:  # Check if logger already has handlers
        if level == "DEBUG":
            # include filename and line number in log output
            formatter = logging.Formatter(
                "%(asctime)s  (%(levelname)s - %(name)s - %(filename)s:%(lineno)d): %(message)s"
            )
        else:
            formatter = logging.Formatter(
                "%(asctime)s  (%(levelname)s - %(name)s): %(message)s"
            )
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger


logger = get_logger(__name__)


class LogQSEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID):
            return obj.hex

        if isinstance(obj, (datetime, date)):
            return obj.isoformat()

        if isinstance(obj, bytes):
            return obj.decode("utf-8")

        if isinstance(obj, decimal.Decimal):
            return float(obj)

        return json.JSONEncoder.default(self, obj)


def output_decorator(func):
    def wrapper(*args, **kwargs):
        if args[0]._pretty:
            return pprint.pprint(func(*args, **kwargs))
        return func(*args, **kwargs)

    return wrapper


class RESTInterface:
    def __init__(self, config, http_client=None):
        self._config = config

        self._headers = {
            "Content-Type": "application/json",
        }

        if (
            self._config.api_key_id is not None
            and self._config.api_key_secret is not None
        ):
            self._headers["Authorization"] = "Bearer " + base64.b64encode(
                bytes(
                    f"{self._config.api_key_id}:{self._config.api_key_secret}", "utf-8"
                )
            ).decode("utf-8")

        self._headers.update(self._config.additional_headers)

        if http_client is None:
            self._client = requests
            self._use_content = False
        else:
            self._client = http_client
            self._use_content = True

    def _get_url_param_string(self, args, exclude=[]):
        url_params = ""
        for key, value in args.items():
            if value is not None and key not in ["self"] + exclude:
                if type(value) == dict or type(value) == list:
                    value = json.dumps(value, cls=LogQSEncoder)
                url_params += f"&{key}={value}"
        if len(url_params) > 0:
            url_params = "?" + url_params[1:]
        return url_params

    def _get_payload_data(self, args, exclude=[]):
        payload = {}
        for key, value in args.items():
            if value is not None and key not in ["self"] + exclude:
                payload[key] = value
        return payload

    def _handle_response_data(self, response):
        if response.status_code == 204:
            return

        content_type = response.headers.get("content-type")
        if content_type == "application/json":
            try:
                response_data = response.json()
            except json.decoder.JSONDecodeError:
                raise Exception(f"Error: {response.text}")
        elif content_type == "text/plain":
            response_data = response.text
        else:
            response_data = response.content

        try:
            if response.ok:
                return response_data
            else:
                raise Exception(response_data)
        except AttributeError:
            if response.is_success:
                return response_data
            else:
                raise Exception(response_data)

    def _handle_retries(self, func, retry_count=None):
        if retry_count is None:
            retry_count = self._config.retry_count
        for i in range(retry_count + 1):
            try:
                return func()
            except Exception as e:
                if not self._config.retry_aggressive:
                    lqs_expected_error_codes = [
                        "[BadRequest]",
                        "[Forbidden]",
                        "[NotFound]",
                        "[Conflict]",
                        "[Locked]",
                    ]
                    for code in lqs_expected_error_codes:
                        if code in str(e):
                            raise e
                if retry_count > 0 and i < retry_count:
                    # exponential backoff
                    backoff = self._config.retry_delay * (2**i)
                    logger.error(f"Error: {e}")
                    logger.info(f"Retrying in {backoff} seconds")
                    time.sleep(backoff)
                else:
                    raise e
        raise Exception("Error: Max retries exceeded")

    def _get_url(self, resource_path):
        prefix = self._config.api_endpoint_prefix or ""
        if self._config.api_url is None:
            return f"{prefix}/{resource_path}"
        elif prefix is None:
            return f"{self._config.api_url}/{resource_path}"
        else:
            if not self._config.api_url.endswith(prefix):
                logger.warning(
                    f"Warning: {self._config.api_url} does not end with {prefix}. "
                    "Using {self._config.api_url}{prefix}/"
                )
                return f"{self._config.api_url}{prefix}/{resource_path}"
            return f"{self._config.api_url}/{resource_path}"

    def _head_resource(self, resource_path):
        url = self._get_url(resource_path)
        if self._config.dry_run:
            logger.info(f"(Dry Run) HEAD {url}")
            return {}

        def make_request():
            r = self._client.head(url, headers=self._headers)
            response_data = self._handle_response_data(r)
            if isinstance(response_data, dict):
                return response_data
            else:
                raise Exception("Error: HEAD request returned non-dict data")

        return self._handle_retries(make_request)

    def _get_resource(
        self,
        resource_path,
        expected_content_type: Optional[str] = "application/json",
        additional_headers=None,
        response_model=None,
    ):
        url = self._get_url(resource_path)
        if self._config.dry_run:
            logger.info(f"(Dry Run) GET {url}")
            return {}

        def make_request():
            headers = self._headers
            if additional_headers:
                headers = {**headers, **additional_headers}
            r = self._client.get(url, headers=headers)
            response_data = self._handle_response_data(r)
            if expected_content_type == "application/json":
                if isinstance(response_data, dict):
                    if response_model:
                        return response_model(**response_data)
                    return response_data
                else:
                    raise Exception("Error: GET request returned non-dict data")
            elif expected_content_type == "text/plain":
                if isinstance(response_data, str):
                    return response_data
                else:
                    raise Exception("Error: GET request returned non-string data")
            else:
                if isinstance(response_data, bytes):
                    return response_data
                else:
                    raise Exception("Error: GET request returned non-bytes data")

        return self._handle_retries(make_request)

    def _create_resource(self, resource_path, data, response_model):
        url = self._get_url(resource_path)
        if self._config.dry_run:
            logger.info(f"(Dry Run) POST {url}, {data}")
            return {}

        def make_request():
            if self._use_content:
                params = dict(
                    url=url,
                    content=json.dumps(data, cls=LogQSEncoder),
                    headers=self._headers,
                )
            else:
                params = dict(
                    url=url,
                    data=json.dumps(data, cls=LogQSEncoder),
                    headers=self._headers,
                )

            r = self._client.post(**params)  # type: ignore
            response_data = self._handle_response_data(r)
            if isinstance(response_data, dict):
                return response_model(**response_data)
            else:
                raise Exception("Error: POST request returned non-dict data")

        return self._handle_retries(make_request)

    def _update_resource(self, resource_path, data, response_model):
        url = self._get_url(resource_path)
        if self._config.dry_run:
            logger.info(f"(Dry Run) PATCH {url}, {data}")
            return {}

        def make_request():
            if self._use_content:
                params = dict(
                    url=url,
                    content=json.dumps(data, cls=LogQSEncoder),
                    headers=self._headers,
                )
            else:
                params = dict(
                    url=url,
                    data=json.dumps(data, cls=LogQSEncoder),
                    headers=self._headers,
                )
            r = self._client.patch(**params)  # type: ignore
            response_data = self._handle_response_data(r)
            if isinstance(response_data, dict):
                return response_model(**response_data)
            else:
                raise Exception("Error: PATCH request returned non-dict data")

        return self._handle_retries(make_request)

    def _delete_resource(self, resource_path):
        url = self._get_url(resource_path)
        if self._config.dry_run:
            logger.info(f"(Dry Run) DELETE {url}")
            return

        def make_request():
            r = self._client.delete(url, headers=self._headers)
            response_data = self._handle_response_data(r)
            if response_data is not None:
                raise Exception(f"Error: DELETE request returned data: {response_data}")

        return self._handle_retries(make_request)
