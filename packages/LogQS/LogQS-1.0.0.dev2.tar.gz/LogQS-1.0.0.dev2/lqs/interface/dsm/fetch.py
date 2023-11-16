from abc import abstractmethod
from uuid import UUID

import lqs.interface.dsm.models as models
from lqs.interface.base.fetch import FetchInterface as BaseFetchInterface


class FetchInterface(BaseFetchInterface):
    @abstractmethod
    def _datastore(self, **kwargs) -> models.DataStoreDataResponse:
        pass

    def datastore(self, datastore_id: UUID):
        return self._datastore(
            datastore_id=datastore_id,
        )

    @abstractmethod
    def _datastore_association(
        self, **kwargs
    ) -> models.DataStoreAssociationDataResponse:
        pass

    def datastore_association(self, datastore_association_id: UUID):
        return self._datastore_association(
            datastore_association_id=datastore_association_id,
        )
