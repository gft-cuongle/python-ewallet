from http.server import BaseHTTPRequestHandler
import json

# A dictionary to store account details
transaction = {"transaction": 1}


class TransactionController(BaseHTTPRequestHandler):

    def do_POST(self):
        """
        Handles POST requests
        """
        if self.path == '/transaction':
            # Return the list of accounts
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(transaction).encode())
        else:
            # Invalid endpoint
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Invalid endpoint')

