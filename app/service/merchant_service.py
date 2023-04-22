# Merchant Service
import uuid

from app.common.account_type import AccountType
from app.repository import merchant_repository
from app.service import account_service


def create_merchant(merchant_name, merchant_url):
    # Create an account with type "merchant"
    merchant_account = account_service.create_account(AccountType.MERCHANT.value)

    merchant = {"merchantName": merchant_name, "accountId": merchant_account.get("accountId"),
                "merchantId": uuid.uuid4().__str__(), "apiKey": uuid.uuid4().__str__(), "merchantUrl": merchant_url}
    merchant_repository.create_merchant(merchant)
    return merchant


def get_merchant_by_id(merchant_id):
    return merchant_repository.get_merchant_by_id(merchant_id)

