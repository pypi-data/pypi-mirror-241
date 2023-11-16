from lqs.interface.dsm import CreateInterface
from lqs.client.common import RESTInterface
import lqs.interface.dsm.models as models


class Create(CreateInterface, RESTInterface):
    def __init__(self, config, http_client=None):
        super().__init__(config=config, http_client=http_client)

    def _api_key(self, **params):
        return self._create_resource("apiKeys", params, models.APIKeyDataResponse)

    def _datastore(self, **params):
        return self._create_resource("dataStores", params, models.DataStoreDataResponse)

    def _datastore_association(self, **params):
        return self._create_resource(
            "dataStoreAssociations", params, models.DataStoreAssociationDataResponse
        )

    def _role(self, **params):
        return self._create_resource("roles", params, models.RoleDataResponse)

    def _user(self, **params):
        return self._create_resource("users", params, models.UserDataResponse)
