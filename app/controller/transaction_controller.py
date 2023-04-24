from http.server import BaseHTTPRequestHandler
import json

from app.utils.response_util import send_failure_response, send_success_response

transaction = {"transaction": 1}


class TransactionController(BaseHTTPRequestHandler):

    def do_POST(self):
        """
        Handles POST requests
        """
        if self.path == '/transaction/create':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(transaction).encode())
            return

        if self.path == '/transaction/confirm':
            # Return the list of accounts
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(transaction).encode())
            return

        if self.path == '/transaction/verify':
            # Return the list of accounts
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(transaction).encode())
            return

        if self.path == '/transaction/cancel':
            # Return the list of accounts
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(transaction).encode())
            return

        else:
            # Invalid endpoint
            send_failure_response(self, 400, b'Invalid endpoint')
