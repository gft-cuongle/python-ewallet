# Account Service
import uuid

from app.repository import account_repository


def create_account(account_type):
    account = {"accountId": uuid.uuid4().__str__(), "accountType": account_type, "balance": 0}
    account_repository.create_account(account)
    return account


def get_account_by_id(account_id):
    return account_repository.get_account_by_id(account_id)
