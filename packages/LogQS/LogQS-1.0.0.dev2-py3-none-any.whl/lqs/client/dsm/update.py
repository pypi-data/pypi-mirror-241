from lqs.interface.dsm import UpdateInterface
from lqs.client.common import RESTInterface
import lqs.interface.dsm.models as models


class Update(UpdateInterface, RESTInterface):
    def __init__(self, config, http_client=None):
        super().__init__(config=config, http_client=http_client)

    def _api_key(self, **params):
        api_key_id = params.pop("api_key_id")
        data = params.pop("data")
        return self._update_resource(
            f"apiKeys/{api_key_id}", data, models.APIKeyDataResponse
        )

    def _datastore(self, **params):
        datastore_id = params.pop("datastore_id")
        data = params.pop("data")
        return self._update_resource(
            f"dataStores/{datastore_id}", data, models.DataStoreDataResponse
        )

    def _datastore_association(self, **params):
        datastore_association_id = params.pop("datastore_association_id")
        data = params.pop("data")
        return self._update_resource(
            f"dataStoreAssociations/{datastore_association_id}",
            data,
            models.DataStoreAssociationDataResponse,
        )

    def _role(self, **params):
        role_id = params.pop("role_id")
        data = params.pop("data")
        return self._update_resource(f"roles/{role_id}", data, models.RoleDataResponse)

    def _user(self, **params):
        user_id = params.pop("user_id")
        data = params.pop("data")
        return self._update_resource(f"users/{user_id}", data, models.UserDataResponse)
