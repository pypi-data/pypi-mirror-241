from lqs.interface.dsm import ListInterface
from lqs.client.common import RESTInterface
import lqs.interface.dsm.models as models


class List(ListInterface, RESTInterface):
    def __init__(self, config, http_client=None):
        super().__init__(config=config, http_client=http_client)

    def _api_key(self, **params):
        resource_path = "apiKeys" + self._get_url_param_string(params, [])
        result = self._get_resource(
            resource_path, response_model=models.APIKeyListResponse
        )
        return result

    def _datastore(self, **params):
        resource_path = "dataStores" + self._get_url_param_string(params, [])
        result = self._get_resource(
            resource_path, response_model=models.DataStoreListResponse
        )
        return result

    def _datastore_association(self, **params):
        resource_path = "dataStoreAssociations" + self._get_url_param_string(params, [])
        result = self._get_resource(
            resource_path, response_model=models.DataStoreAssociationListResponse
        )
        return result

    def _role(self, **params):
        resource_path = "roles" + self._get_url_param_string(params, [])
        result = self._get_resource(
            resource_path, response_model=models.RoleListResponse
        )
        return result

    def _user(self, **params):
        resource_path = "users" + self._get_url_param_string(params, [])
        result = self._get_resource(
            resource_path, response_model=models.UserListResponse
        )
        return result
