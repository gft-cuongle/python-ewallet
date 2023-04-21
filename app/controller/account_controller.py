from http.server import BaseHTTPRequestHandler
import json

# A dictionary to store account details
accounts = {"id": 1, "name": "this's a name"}


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
            self.wfile.write(json.dumps(accounts).encode())
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
            account_id = account_data.get('id')
            if account_id is None:
                # Account ID is mandatory
                self.send_response(400)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(b'Account ID is mandatory')
                return
            accounts[account_id] = account_data
            self.send_response(201)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(account_data).encode())
        else:
            # Invalid endpoint
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Invalid endpoint')
