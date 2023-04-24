from enum import Enum


class TransactionStatus(Enum):
    INITIALIZED = "INITIALIZED"
    CONFIRMED = "CONFIRMED"
    VERIFIED = "VERIFIED"
    COMPLETED = "COMPLETED"
    CANCELED = "CANCELED"
    EXPIRED = "EXPIRED"
    FAILED = "FAILED"


def get_transaction_status_by_value(status):
    for trx_status in TransactionStatus:
        if trx_status.value == status:
            return trx_status
    return None
