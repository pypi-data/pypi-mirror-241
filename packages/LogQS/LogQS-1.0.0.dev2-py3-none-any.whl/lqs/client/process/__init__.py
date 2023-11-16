from lqs.client.process.list import List
from lqs.client.process.fetch import Fetch
from lqs.client.process.create import Create
from lqs.client.process.update import Update
from lqs.client.process.delete import Delete

import os
import logging

logging.basicConfig(
    level=os.getenv("LQS_LOG_LEVEL") or logging.INFO,
    format="%(asctime)s  (%(levelname)s - %(name)s): %(message)s",
)
logger = logging.getLogger(__name__)


class Process:
    def __init__(
        self,
        config,
        http_client=None,
    ):
        self.config = config.model_copy()

        # infer INGEST API URL from LQS API URL
        url = self.config.api_url
        if url is not None and not url.endswith("/process/api"):
            index_of_lqs = url.find("/lqs")
            if index_of_lqs != -1:
                url = url[:index_of_lqs] + "/process/api"
            else:
                url = url + "/process/api"
            self.config.api_url = url

        self.list = List(config=self.config, http_client=http_client)
        self.fetch = Fetch(config=self.config, http_client=http_client)
        self.create = Create(config=self.config, http_client=http_client)
        self.update = Update(config=self.config, http_client=http_client)
        self.delete = Delete(config=self.config, http_client=http_client)
