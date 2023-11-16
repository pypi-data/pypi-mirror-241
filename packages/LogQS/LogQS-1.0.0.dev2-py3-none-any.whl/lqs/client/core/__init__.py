from lqs.client.core.list import List
from lqs.client.core.fetch import Fetch
from lqs.client.core.create import Create
from lqs.client.core.update import Update
from lqs.client.core.delete import Delete

import os
import logging

logging.basicConfig(
    level=os.getenv("LQS_LOG_LEVEL") or logging.INFO,
    format="%(asctime)s  (%(levelname)s - %(name)s): %(message)s",
)
logger = logging.getLogger(__name__)


class LogQS:
    def __init__(
        self,
        config,
        http_client=None,
    ):
        self.config = config

        self.list = List(config=self.config, http_client=http_client)
        self.fetch = Fetch(config=self.config, http_client=http_client)
        self.create = Create(config=self.config, http_client=http_client)
        self.update = Update(config=self.config, http_client=http_client)
        self.delete = Delete(config=self.config, http_client=http_client)
