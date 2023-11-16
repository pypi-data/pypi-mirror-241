from lqs.client.config import ClientConfig
from lqs.client.core import LogQS
from lqs.client.dsm import DataStoreManager
from lqs.client.process import Process
from lqs.client.utils import Utils

import os
import logging

logging.basicConfig(
    level=os.getenv("LQS_LOG_LEVEL") or logging.INFO,
    format="%(asctime)s  (%(levelname)s - %(name)s): %(message)s",
)
logger = logging.getLogger(__name__)


class Client:
    def __init__(
        self,
        api_url=None,
        api_key_id=None,
        api_key_secret=None,
        api_endpoint_prefix=None,
        pretty=None,
        verbose=None,
        dry_run=None,
        retry_count=None,
        retry_delay=None,
        retry_aggressive=None,
        additional_headers=None,
        http_client=None,
    ):
        params = locals()
        params.pop("self")
        params.pop("http_client")
        self.config = ClientConfig(**{k: v for k, v in params.items() if v is not None})

        self.lqs = LogQS(config=self.config, http_client=http_client)
        self.dsm = DataStoreManager(config=self.config, http_client=http_client)
        self.process = Process(config=self.config, http_client=http_client)

        # Expose these directly for convenience
        self.list = self.lqs.list
        self.fetch = self.lqs.fetch
        self.create = self.lqs.create
        self.update = self.lqs.update
        self.delete = self.lqs.delete

        self.utils = Utils(client=self)
