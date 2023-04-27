from http.server import BaseHTTPRequestHandler
import json

from app.common.account_type import AccountType
from app.service.transaction_service import init_transaction
from app.service import token_service, merchant_service, account_service, transaction_service
from app.utils.response_util import send_failure_response, send_success_response


class TransactionController(BaseHTTPRequestHandler):

    def do_POST(self):
        """
        Handles POST requests
        """
        if self.path == '/transaction/create':
            content_length = int(self.headers['Content-Length'])
            token = token_service.decode_token(self.headers['Authentication'])
            if token is None:
                send_failure_response(self, 400, b'Invalid token')
                return
            # Validate account type
            if token["accountType"] != AccountType.MERCHANT.value:
                send_failure_response(self, 400, b'Only account type MERCHANT is allowed to Init Transaction')
                return
            post_data = self.rfile.read(content_length)
            account_data = json.loads(post_data.decode())
            merchant_id = account_data.get('merchantId')
            amount = account_data.get('amount')
            extra_data = account_data.get('extraData')
            signature = account_data.get('signature')

            # Validate merchant
            merchant = merchant_service.get_merchant_by_id(merchant_id)
            if merchant is None:
                send_failure_response(self, 404, b'Merchant not found')
                return

            transaction = init_transaction(merchant, amount, extra_data, signature)
            send_success_response(self, 200, json.dumps(transaction).encode())
            return

        if self.path == '/transaction/confirm':
            content_length = int(self.headers['Content-Length'])
            token = token_service.decode_token(self.headers['Authentication'])
            if token is None:
                send_failure_response(self, 400, b'Invalid token')
                return
            # Validate account type
            if token["accountType"] != AccountType.PERSONAL.value:
                send_failure_response(self, 400, b'Only account type PERSONAL is allowed to Confirm Transaction')
                return
            post_data = self.rfile.read(content_length)
            account_data = json.loads(post_data.decode())
            transaction_id = account_data.get('transactionId')

            # Validate personal account
            account = account_service.get_account_by_id(token["accountId"])
            if account is None:
                send_failure_response(self, 404, b'Account not found')
                return

            # Validate transaction
            tranx = transaction_service.get_transaction_by_id(transaction_id)
            if tranx is None:
                send_failure_response(self, 404, b'Transaction not found')

            message = transaction_service.confirm_transaction(account, tranx)
            if message != "success":
                send_failure_response(self, 400,
                                      json.dumps({"code": "ERR", "message": message}).encode())
                return
            send_success_response(self, 200, json.dumps({"code": "SUC", "message": message}).encode())
            return

        if self.path == '/transaction/verify':
            content_length = int(self.headers['Content-Length'])
            token = token_service.decode_token(self.headers['Authentication'])
            if token is None:
                send_failure_response(self, 400, b'Invalid token')
                return
            # Validate account type
            if token["accountType"] != AccountType.PERSONAL.value:
                send_failure_response(self, 400, b'Only account type PERSONAL is allowed to Confirm Transaction')
                return
            post_data = self.rfile.read(content_length)
            account_data = json.loads(post_data.decode())
            transaction_id = account_data.get('transactionId')

            # Validate personal account
            account = account_service.get_account_by_id(token["accountId"])
            if account is None:
                send_failure_response(self, 404, b'Account not found')
                return

            # Validate transaction
            tranx = transaction_service.get_transaction_by_id(transaction_id)
            if tranx is None:
                send_failure_response(self, 404, b'Transaction not found')

            message = transaction_service.verify_transaction(account, tranx)
            if message != "success":
                send_failure_response(self, 400,
                                      json.dumps({"code": "ERR", "message": message}).encode())
                return
            send_success_response(self, 200, json.dumps({"code": "SUC", "message": message}).encode())
            return

        if self.path == '/transaction/cancel':
            send_success_response(self, 200, b'TODO')
            return

        else:
            # Invalid endpoint
            send_failure_response(self, 400, b'Invalid endpoint')
