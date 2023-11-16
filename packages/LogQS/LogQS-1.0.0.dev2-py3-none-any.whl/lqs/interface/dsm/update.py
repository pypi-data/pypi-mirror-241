from abc import abstractmethod
from uuid import UUID

import lqs.interface.dsm.models as models
from lqs.interface.base.update import UpdateInterface as BaseUpdateInterface


class UpdateInterface(BaseUpdateInterface):
    @abstractmethod
    def _datastore(self, **kwargs) -> models.DataStoreDataResponse:
        pass

    def datastore(self, datastore_id: UUID, data: dict):
        return self._datastore(
            datastore_id=datastore_id,
            data=self._process_data(data),
        )

    def _datastore_by_model(
        self, datastore_id: UUID, data: models.DataStoreUpdateRequest
    ):
        return self._datastore(
            datastore_id=datastore_id,
            data=data.model_dump(exclude_unset=True),
        )

    @abstractmethod
    def _datastore_association(
        self, **kwargs
    ) -> models.DataStoreAssociationDataResponse:
        pass

    def datastore_association(self, datastore_association_id: UUID, data: dict):
        return self._datastore_association(
            datastore_association_id=datastore_association_id,
            data=self._process_data(data),
        )

    def _datastore_association_by_model(
        self,
        datastore_association_id: UUID,
        data: models.DataStoreAssociationUpdateRequest,
    ):
        return self._datastore_association(
            datastore_association_id=datastore_association_id,
            data=data.model_dump(exclude_unset=True),
        )
