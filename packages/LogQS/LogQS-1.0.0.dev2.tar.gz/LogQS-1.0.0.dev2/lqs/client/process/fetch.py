from lqs.interface.process import FetchInterface
from lqs.client.common import RESTInterface
import lqs.interface.process.models as models


class Fetch(FetchInterface, RESTInterface):
    def __init__(self, config, http_client=None):
        super().__init__(config=config, http_client=http_client)

    def _event(self, **params):
        event_id = params.pop("event_id")
        result = self._get_resource(
            f"events/{event_id}", response_model=models.EventDataResponse
        )
        return result

    def _job(self, **params):
        job_id = params.pop("job_id")
        result = self._get_resource(
            f"jobs/{job_id}", response_model=models.JobDataResponse
        )
        return result
