from lqs.interface.process import ListInterface
from lqs.client.common import RESTInterface
import lqs.interface.process.models as models


class List(ListInterface, RESTInterface):
    def __init__(self, config, http_client=None):
        super().__init__(config=config, http_client=http_client)

    def _event(self, **params):
        resource_path = "events" + self._get_url_param_string(params, [])
        result = self._get_resource(
            resource_path, response_model=models.EventListResponse
        )
        return result

    def _job(self, **params):
        resource_path = "jobs" + self._get_url_param_string(params, [])
        result = self._get_resource(
            resource_path, response_model=models.JobListResponse
        )
        return result
