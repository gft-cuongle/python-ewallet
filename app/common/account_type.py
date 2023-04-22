from enum import Enum


class AccountType(Enum):
    PERSONAL = "personal"
    MERCHANT = "merchant"
    ISSUER = "issuer"


def get_account_type_by_value(acc_type):
    for account_type in AccountType:
        if account_type.value == acc_type:
            return account_type
    return None
