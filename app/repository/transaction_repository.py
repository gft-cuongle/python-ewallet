import time

from tinydb import TinyDB, Query, where

from app.common.transaction_status import TransactionStatus

# Open the JSON file for reading and writing
db = TinyDB('resources/transaction_database.json')


def init_transaction(transaction):
    db.insert(transaction)
    return True


def get_all_not_completed_transaction():
    return db.search(
        (where("status") == TransactionStatus.INITIALIZED.value) |
        (where("status") == TransactionStatus.CONFIRMED.value) |
        (where("status") == TransactionStatus.VERIFIED.value)
    )


def update_transaction_status(transaction_id, status):
    return db.update({'status': status, 'updatedTime': int(time.time() * 1000)},
                     where("transactionId") == str(transaction_id))


def update_confirm_transaction(transaction_id, personal_account_id):
    db.update({'status': TransactionStatus.CONFIRMED.value, 'outcomeAccount': personal_account_id,
               'updatedTime': int(time.time() * 1000)}, where("transactionId") == str(transaction_id))
    return True


def update_verify_transaction(transaction_id, personal_account_id):
    db.update({'status': TransactionStatus.VERIFIED.value, 'outcomeAccount': personal_account_id,
               'updatedTime': int(time.time() * 1000)}, where("transactionId") == str(transaction_id))
    return True


def get_transaction_by_id(transaction_id):
    transaction = db.search(where("transactionId") == str(transaction_id))
    if transaction is not None and len(transaction) > 0:
        return transaction[0]
    else:
        return None
