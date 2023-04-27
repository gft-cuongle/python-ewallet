# Account Service
import uuid

from app.repository import account_repository


def create_account(account_type):
    account = {"accountId": uuid.uuid4().__str__(), "accountType": account_type, "balance": 0}
    account_repository.create_account(account)
    return account


def get_account_by_id(account_id):
    return account_repository.get_account_by_id(account_id)


def topup_account(receiver_account_id, issuer_account_id, amount):
    receiver = account_repository.get_account_by_id(receiver_account_id)
    receiver_balance = receiver["balance"]
    account_repository.update_account_balance(receiver_account_id, receiver_balance + amount)

    issuer = account_repository.get_account_by_id(issuer_account_id)
    issuer_balance = issuer["balance"]
    account_repository.update_account_balance(issuer_account_id, issuer_balance - amount)


def transfer_account_balance(income_account_id, outcome_account_id, amount):
    income = account_repository.get_account_by_id(income_account_id)
    income_balance = income["balance"]
    account_repository.update_account_balance(income_account_id, income_balance + amount)

    outcome = account_repository.get_account_by_id(outcome_account_id)
    outcome_balance = outcome["balance"]
    account_repository.update_account_balance(outcome_account_id, outcome_balance - amount)


def get_all_account():
    return account_repository.get_all_account()
