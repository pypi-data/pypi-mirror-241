from abc import abstractmethod
from uuid import UUID

from lqs.interface.base.delete import DeleteInterface as BaseDeleteInterface


class DeleteInterface(BaseDeleteInterface):
    @abstractmethod
    def _datastore(self, **kwargs):
        pass

    def datastore(self, datastore_id: UUID):
        return self._datastore(
            datastore_id=datastore_id,
        )

    @abstractmethod
    def _datastore_association(self, **kwargs):
        pass

    def datastore_association(self, datastore_association_id: UUID):
        return self._datastore_association(
            datastore_association_id=datastore_association_id,
        )
