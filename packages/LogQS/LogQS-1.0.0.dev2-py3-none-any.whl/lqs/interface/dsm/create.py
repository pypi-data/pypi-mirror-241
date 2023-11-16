from abc import abstractmethod
from typing import Optional
from uuid import UUID

from lqs.interface.base.create import CreateInterface as BaseCreateInterface
import lqs.interface.dsm.models as models


class CreateInterface(BaseCreateInterface):
    @abstractmethod
    def _datastore(self, **kwargs) -> models.DataStoreDataResponse:
        pass

    def datastore(self, name: str):
        return self._datastore(name=name)

    def _datastore_by_model(self, data: models.DataStoreCreateRequest):
        return self.datastore(**data.model_dump())

    @abstractmethod
    def _datastore_association(
        self, **kwargs
    ) -> models.DataStoreAssociationDataResponse:
        pass

    def datastore_association(
        self,
        user_id: UUID,
        datastore_id: UUID,
        owner: bool = False,
        datastore_user_id: Optional[UUID] = None,
        datastore_username: Optional[str] = None,
        datastore_role_id: Optional[UUID] = None,
        datastore_admin: bool = False,
        datastore_disabled: bool = False,
    ):
        return self._datastore_association(
            user_id=user_id,
            datastore_id=datastore_id,
            datastore_user_id=datastore_user_id,
            owner=owner,
            datastore_username=datastore_username,
            datastore_role_id=datastore_role_id,
            datastore_admin=datastore_admin,
            datastore_disabled=datastore_disabled,
        )

    def _datastore_association_by_model(
        self, data: models.DataStoreAssociationCreateRequest
    ):
        return self.datastore_association(**data.model_dump())
