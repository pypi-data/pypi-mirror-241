from uuid import UUID

from lqs.interface.dsm import DeleteInterface
from lqs.client.common import RESTInterface

# TODO: make this consistent with other interfaces


class Delete(DeleteInterface, RESTInterface):
    def __init__(self, config, http_client=None):
        super().__init__(config=config, http_client=http_client)

    def _api_key(self, api_key_id: UUID):
        self._delete_resource(f"apiKeys/{api_key_id}")
        return

    def _datastore(self, datastore_id: UUID):
        self._delete_resource(f"dataStores/{datastore_id}")
        return

    def _datastore_association(self, datastore_association_id: UUID):
        self._delete_resource(f"dataStoreAssociations/{datastore_association_id}")
        return

    def _role(self, role_id: UUID):
        self._delete_resource(f"roles/{role_id}")
        return

    def _user(self, user_id: UUID):
        self._delete_resource(f"users/{user_id}")
        return
