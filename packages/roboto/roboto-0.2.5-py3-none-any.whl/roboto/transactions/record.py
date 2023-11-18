import datetime
import enum
import typing

import pydantic


class TransactionType(str, enum.Enum):
    FileUpload = "file_upload"


class TransactionStatus(str, enum.Enum):
    Pending = "pending"
    Completed = "completed"


class TransactionRecord(pydantic.BaseModel):
    org_id: str
    transaction_id: str
    transaction_type: TransactionType
    transaction_status: TransactionStatus
    origination: str
    resource_count: int = 0
    expected_resource_count: typing.Optional[int] = None
    created: datetime.datetime
    created_by: str
    modified: datetime.datetime
    modified_by: str

    class Config:
        extra = pydantic.Extra.forbid
