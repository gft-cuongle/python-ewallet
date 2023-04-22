from http.server import BaseHTTPRequestHandler

from app.common.account_type import AccountType, get_account_type_by_value
from app.service import account_service
import json


class AccountController(BaseHTTPRequestHandler):

    def do_GET(self):
        """
        Handles GET requests
        """
        if self.path == '/account/123/token':
            # Return the list of accounts
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            acc = account_service.get_account_by_id("1ff41c84-5788-4f42-988a-b6c0e685e570")
            self.wfile.write(json.dumps(acc).encode())
        else:
            # Invalid endpoint
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Invalid endpoint')

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
                self.send_response(400)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(b'Account type is mandatory')
                return

            if get_account_type_by_value(account_type) is None:
                self.send_response(400)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(b'Account type is not valid')
                return

            account = account_service.create_account(account_type)

            self.send_response(201)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(account).encode())
        else:
            # Invalid endpoint
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Invalid endpoint')
