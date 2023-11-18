import typing

from ..exceptions import RobotoHttpExceptionParse
from ..http import HttpClient, roboto_headers
from ..serde import pydantic_jsonable_dict
from .http_resources import (
    BeginTransactionRequest,
)
from .manager_abc import TransactionManagerABC
from .record import (
    TransactionRecord,
    TransactionType,
)


class TransactionManager(TransactionManagerABC):
    __http_client: HttpClient
    __roboto_service_base_url: str

    def __init__(self, roboto_service_base_url: str, http_client: HttpClient) -> None:
        self.__http_client = http_client
        self.__roboto_service_base_url = roboto_service_base_url

    def begin_transaction(
        self,
        transaction_type: TransactionType,
        origination: str,
        expected_resource_count: typing.Optional[int] = None,
        org_id: typing.Optional[str] = None,
        caller: typing.Optional[str] = None,
        resource_owner_id: typing.Optional[str] = None,
    ) -> TransactionRecord:
        url = f"{self.__roboto_service_base_url}/v1/transactions/begin"
        request_body = BeginTransactionRequest(
            transaction_type=transaction_type,
            origination=origination,
            expected_resource_count=expected_resource_count,
        )

        with RobotoHttpExceptionParse():
            response = self.__http_client.post(
                url,
                data=pydantic_jsonable_dict(
                    request_body, exclude_none=True, exclude_unset=True
                ),
                headers=roboto_headers(
                    org_id=org_id,
                    user_id=caller,
                    resource_owner_id=resource_owner_id,
                    additional_headers={"Content-Type": "application/json"},
                ),
            )

        return TransactionRecord.parse_obj(response.from_json(json_path=["data"]))

    def end_transaction(
        self,
        transaction_id: str,
        caller: typing.Optional[str] = None,
        org_id: typing.Optional[str] = None,
        resource_owner_id: typing.Optional[str] = None,
    ) -> None:
        url = (
            f"{self.__roboto_service_base_url}/v1/transactions/id/{transaction_id}/end"
        )
        with RobotoHttpExceptionParse():
            self.__http_client.put(
                url,
                headers=roboto_headers(
                    org_id=org_id,
                    user_id=caller,
                    resource_owner_id=resource_owner_id,
                    additional_headers={"Content-Type": "application/json"},
                ),
            )

    def get_transaction(
        self,
        transaction_id: str,
        org_id: typing.Optional[str] = None,
        resource_owner_id: typing.Optional[str] = None,
    ) -> TransactionRecord:
        url = f"{self.__roboto_service_base_url}/v1/transactions/id/{transaction_id}"
        with RobotoHttpExceptionParse():
            response = self.__http_client.get(
                url,
                headers=roboto_headers(
                    org_id=org_id,
                    resource_owner_id=resource_owner_id,
                    additional_headers={"Content-Type": "application/json"},
                ),
            )

        return TransactionRecord.parse_obj(response.from_json(json_path=["data"]))
