#  Copyright (c) 2023 Roboto Technologies, Inc.

from typing import Any

from roboto.exceptions import (
    RobotoHttpExceptionParse,
)
from roboto.http import HttpClient


class NotificationsClient:
    __http_client: HttpClient

    def __init__(self, http_client: HttpClient):
        super().__init__()
        self.__http_client = http_client

    def get_notifications(self) -> dict[str, Any]:
        url = self.__http_client.url("v1/notifications")

        with RobotoHttpExceptionParse():
            response = self.__http_client.get(url=url)

            return response.from_json(json_path=["data"])

    def update_notification(self, notification_id: str, read_status: str) -> Any:
        url = self.__http_client.url(f"v1/notifications/{notification_id}")

        body = {
            "read_status": read_status,
        }

        with RobotoHttpExceptionParse():
            response = self.__http_client.put(
                url=url,
                data=body,
            )

            return response.from_json(json_path=["data"])

    def delete_notification(self, notification_id: str) -> None:
        url = self.__http_client.url(f"v1/notifications/{notification_id}")

        with RobotoHttpExceptionParse():
            self.__http_client.delete(
                url=url,
            )

            return None
