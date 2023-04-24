import json
import re
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse

from app.common.account_type import get_account_type_by_value, AccountType
from app.service import account_service
from app.service import token_service
from app.utils.response_util import send_failure_response, send_success_response


class AccountController(BaseHTTPRequestHandler):

    def do_GET(self):
        """
        Handles GET requests for /account/{accountUUID}/token
        """
        re_acc_token = r'^/account/[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}/token$'
        parsed_url = urlparse(self.path)
        if re.match(re_acc_token, parsed_url.path):
            # Extract the accountUUID from the URL
            account_uuid = parsed_url.path.split('/')[2]

            account = account_service.get_account_by_id(account_uuid)
            if account is None:
                send_failure_response(self, 404, b'Account not found')
                return

            token = token_service.create_account_token(account)
            send_success_response(self, 200, json.dumps(token).encode())
            return

        if self.path == "/account/all":
            accounts = account_service.get_all_account()
            send_success_response(self, 200, json.dumps(accounts).encode())
            return

        # Invalid endpoint
        send_failure_response(self, 404, b'Invalid endpoint')

    def do_POST(self):
        """
        Handles POST requests
        """
        if self.path == '/account':
            # Create a new account
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            account_data = json.loads(post_data.decode())
            account_type = account_data.get('accountType')
            if account_type is None:
                # Account type is mandatory
                send_failure_response(self, 400, b'Account type is mandatory')
                return

            if get_account_type_by_value(account_type) is None:
                send_failure_response(self, 400, b'Account type is not valid')
                return

            account = account_service.create_account(account_type)
            send_success_response(self, 201, json.dumps(account).encode())
            return

        if self.path == "/account/topup":
            content_length = int(self.headers['Content-Length'])
            token = token_service.decode_token(self.headers['Authentication'])
            if token is None:
                send_failure_response(self, 400, b'Invalid token')
                return
            # Validate account type
            if token["accountType"] != AccountType.ISSUER.value:
                send_failure_response(self, 400, b'Only account type ISSUER is allowed to TOP UP')
                return
            post_data = self.rfile.read(content_length)
            account_data = json.loads(post_data.decode())
            account_id = account_data.get('accountId')
            amount = account_data.get('amount')

            # Validate receiver account
            account = account_service.get_account_by_id(account_id)
            if account is None:
                send_failure_response(self, 400, b'Account not found')
                return

            # Validate issuer account
            issuer_account = account_service.get_account_by_id(token["accountId"])
            if issuer_account is None:
                send_failure_response(self, 400, b'Issuer account not found')
                return

            account_service.topup_account(account_id, token["accountId"], amount)
            send_success_response(self, 200, json.dumps("top up success").encode())
            return

        # Invalid endpoint
        send_failure_response(self, 404, b'Invalid endpoint')
