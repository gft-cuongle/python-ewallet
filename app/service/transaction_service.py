import time
import uuid

from app.common.transaction_status import TransactionStatus
from app.repository import transaction_repository


def init_transaction(merchant, amount, extra_data, signature):
    transaction = {"transactionId": uuid.uuid4().__str__(),
                   "merchantId": merchant.get("merchantId"),
                   "incomeAccount": merchant.get("accountId"),
                   "outcomeAccount": None,
                   "amount": amount,
                   "extraData": extra_data,
                   "signature": signature,
                   "status": TransactionStatus.INITIALIZED.value,
                   "createdTime": int(time.time() * 1000),
                   "updatedTime": int(time.time() * 1000)
                   }
    transaction_repository.init_transaction(transaction)
    return transaction


def get_all_not_completed_transaction():
    return transaction_repository.get_all_not_completed_transaction()


def update_transaction_status(transaction_id, status):
    return transaction_repository.update_transaction_status(transaction_id, status)


def get_transaction_by_id(transaction_id):
    return transaction_repository.get_transaction_by_id(transaction_id)


def confirm_transaction(account, tranx):
    # Validate transaction before set status to confirm
    if tranx["status"] != TransactionStatus.INITIALIZED.value:
        return "Transaction status is not INITIALIZED"
    if account["balance"] < tranx["amount"]:
        update_transaction_status(tranx["transactionId"], TransactionStatus.FAILED.value)
        return "Account balance is not enough"
    transaction_repository.update_confirm_transaction(tranx["transactionId"], account["accountId"])
    return "success"
