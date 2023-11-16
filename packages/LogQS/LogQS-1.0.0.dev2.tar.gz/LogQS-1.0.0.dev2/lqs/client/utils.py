import os
from typing import TYPE_CHECKING
from concurrent.futures import ThreadPoolExecutor

import requests

if TYPE_CHECKING:
    from lqs.client import Client


class Utils:
    def __init__(self, client: "Client"):
        self.client = client

    def upload_log_object(
        self,
        log_id: str,
        file_path: str,
        object_key: str = None,
        part_size: int = 5 * 1024 * 1024,
        max_workers: int | None = 8,
    ):
        if object_key is None:
            object_key = file_path.split("/")[-1]

        log_object = self.client.create.log_object(
            log_id=log_id,
            key=object_key,
        ).data

        object_size = os.path.getsize(file_path)
        number_of_parts = object_size // part_size + 1
        log_object_parts = []
        if max_workers is not None:
            futures = []
            with ThreadPoolExecutor(max_workers=max_workers) as executor:
                for idx in range(0, number_of_parts):
                    offset = idx * part_size
                    with open(file_path, "rb") as f:
                        f.seek(offset)
                        data = f.read(part_size)
                        futures.append(
                            executor.submit(
                                self.upload_log_object_part,
                                log_id=log_id,
                                object_key=object_key,
                                size=len(data),
                                part_number=idx + 1,
                                data=data,
                            )
                        )

                for future in futures:
                    log_object_parts.append(future.result())
        else:
            for idx in range(0, number_of_parts):
                offset = idx * part_size
                with open(file_path, "rb") as f:
                    f.seek(offset)
                    data = f.read(part_size)
                    log_object_parts.append(
                        self.upload_log_object_part(
                            log_id=log_id,
                            object_key=object_key,
                            size=len(data),
                            part_number=idx + 1,
                            data=data,
                        )
                    )

        log_object = self.client.update.log_object(
            log_id=log_id, object_key=object_key, data={"upload_state": "complete"}
        ).data

        return log_object, log_object_parts

    def upload_log_object_part(self, log_id, object_key, size, part_number, data):
        object_part = self.client.create.log_object_part(
            log_id=log_id,
            object_key=object_key,
            size=size,
            part_number=part_number,
        ).data

        upload_object_data_url = object_part.presigned_url
        response = requests.put(
            upload_object_data_url,
            data=data,
        )

        if response.status_code != 200:
            raise Exception(f"Error while uploading object part: {response.text}")

        return self.client.fetch.log_object_part(
            log_id=log_id,
            object_key=object_key,
            part_number=part_number,
        ).data
