import abc
import typing

from .record import (
    TransactionRecord,
    TransactionType,
)


class TransactionManagerABC(abc.ABC):
    @abc.abstractmethod
    def begin_transaction(
        self,
        transaction_type: TransactionType,
        origination: str,
        expected_resource_count: typing.Optional[int] = None,
        org_id: typing.Optional[str] = None,
        caller: typing.Optional[str] = None,
        resource_owner_id: typing.Optional[str] = None,
    ) -> TransactionRecord:
        raise NotImplementedError("begin_transaction")

    @abc.abstractmethod
    def end_transaction(
        self,
        transaction_id: str,
        caller: typing.Optional[str] = None,
        org_id: typing.Optional[str] = None,
        resource_owner_id: typing.Optional[str] = None,
    ) -> None:
        raise NotImplementedError("end_transaction")

    @abc.abstractmethod
    def get_transaction(
        self,
        transaction_id: str,
        org_id: typing.Optional[str] = None,
        resource_owner_id: typing.Optional[str] = None,
    ) -> TransactionRecord:
        raise NotImplementedError("get_transaction")
