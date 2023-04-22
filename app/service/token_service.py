from app.utils import token_util


def create_account_token(account):
    return token_util.init_jwt_token(account)
