from typing import Optional
from datetime import datetime
from uuid import UUID
from abc import abstractmethod

import lqs.interface.dsm.models as models
from lqs.interface.base.list import ListInterface as BaseListInterface


class ListInterface(BaseListInterface):
    @abstractmethod
    def _datastore(self, **kwargs) -> models.DataStoreListResponse:
        pass

    def datastore(
        self,
        offset: Optional[int] = 0,
        limit: Optional[int] = 10,
        order: Optional[str] = "created_at",
        sort: Optional[str] = "ASC",
        name: Optional[str] = None,
        name_like: Optional[str] = None,
        created_by: Optional[UUID] = None,
        updated_by: Optional[UUID] = None,
        deleted_by: Optional[UUID] = None,
        updated_by_null: Optional[bool] = None,
        deleted_by_null: Optional[bool] = None,
        updated_at_null: Optional[bool] = None,
        deleted_at_null: Optional[bool] = None,
        created_at_lte: Optional[datetime] = None,
        updated_at_lte: Optional[datetime] = None,
        deleted_at_lte: Optional[datetime] = None,
        created_at_gte: Optional[datetime] = None,
        updated_at_gte: Optional[datetime] = None,
        deleted_at_gte: Optional[datetime] = None,
    ):
        return self._datastore(
            offset=offset,
            limit=limit,
            order=order,
            sort=sort,
            name=name,
            name_like=name_like,
            created_by=created_by,
            updated_by=updated_by,
            deleted_by=deleted_by,
            updated_by_null=updated_by_null,
            deleted_by_null=deleted_by_null,
            updated_at_null=updated_at_null,
            deleted_at_null=deleted_at_null,
            created_at_lte=created_at_lte,
            updated_at_lte=updated_at_lte,
            deleted_at_lte=deleted_at_lte,
            created_at_gte=created_at_gte,
            updated_at_gte=updated_at_gte,
            deleted_at_gte=deleted_at_gte,
        )

    def datastores(self, **kwargs):
        return self.datastore(**kwargs)

    @abstractmethod
    def _datastore_association(
        self, **kwargs
    ) -> models.DataStoreAssociationListResponse:
        pass

    def datastore_association(
        self,
        offset: Optional[int] = 0,
        limit: Optional[int] = 10,
        order: Optional[str] = "created_at",
        sort: Optional[str] = "ASC",
        user_id: Optional[UUID] = None,
        datastore_id: Optional[UUID] = None,
        datastore_user_id: Optional[UUID] = None,
        created_by: Optional[UUID] = None,
        updated_by: Optional[UUID] = None,
        deleted_by: Optional[UUID] = None,
        updated_by_null: Optional[bool] = None,
        deleted_by_null: Optional[bool] = None,
        updated_at_null: Optional[bool] = None,
        deleted_at_null: Optional[bool] = None,
        created_at_lte: Optional[datetime] = None,
        updated_at_lte: Optional[datetime] = None,
        deleted_at_lte: Optional[datetime] = None,
        created_at_gte: Optional[datetime] = None,
        updated_at_gte: Optional[datetime] = None,
        deleted_at_gte: Optional[datetime] = None,
    ):
        return self._datastore_association(
            user_id=user_id,
            datastore_id=datastore_id,
            datastore_user_id=datastore_user_id,
            offset=offset,
            limit=limit,
            order=order,
            sort=sort,
            created_by=created_by,
            updated_by=updated_by,
            deleted_by=deleted_by,
            updated_by_null=updated_by_null,
            deleted_by_null=deleted_by_null,
            updated_at_null=updated_at_null,
            deleted_at_null=deleted_at_null,
            created_at_lte=created_at_lte,
            updated_at_lte=updated_at_lte,
            deleted_at_lte=deleted_at_lte,
            created_at_gte=created_at_gte,
            updated_at_gte=updated_at_gte,
            deleted_at_gte=deleted_at_gte,
        )

    def datastore_associations(self, **kwargs):
        return self.datastore_association(**kwargs)
