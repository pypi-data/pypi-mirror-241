from lqs.interface.process import UpdateInterface
from lqs.client.common import RESTInterface
import lqs.interface.process.models as models


class Update(UpdateInterface, RESTInterface):
    def __init__(self, config, http_client=None):
        super().__init__(config=config, http_client=http_client)

    def _event(self, **params):
        event_id = params.pop("event_id")
        data = params.pop("data")
        return self._update_resource(
            f"events/{event_id}", data, models.EventDataResponse
        )

    def _job(self, **params):
        job_id = params.pop("job_id")
        data = params.pop("data")
        return self._update_resource(f"jobs/{job_id}", data, models.JobDataResponse)
