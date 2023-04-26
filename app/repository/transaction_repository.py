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
        where("status") != TransactionStatus.COMPLETED.value
        and where("status") != TransactionStatus.EXPIRED.value)


def update_transaction_status(transaction_id, status):
    db.update({'status': status}, where("transactionId") == str(transaction_id))
    return db.update({'updatedTime': time.time() * 1000}, where("transactionId") == str(transaction_id))
