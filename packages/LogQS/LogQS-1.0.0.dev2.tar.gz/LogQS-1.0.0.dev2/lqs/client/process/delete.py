from uuid import UUID

from lqs.interface.process import DeleteInterface

from lqs.client.common import RESTInterface

# TODO: make this consistent with other interfaces


class Delete(DeleteInterface, RESTInterface):
    def __init__(self, config, http_client=None):
        super().__init__(config=config, http_client=http_client)

    def _event(self, event_id: UUID):
        self._delete_resource(f"events/{event_id}")
        return

    def _job(self, job_id: UUID):
        self._delete_resource(f"jobs/{job_id}")
        return
