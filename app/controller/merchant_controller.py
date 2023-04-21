from http.server import BaseHTTPRequestHandler
import json

# A dictionary to store account details
merchants = {"merchant": 1}


class MerchantController(BaseHTTPRequestHandler):

    def do_POST(self):
        """
        Handles POST requests
        """
        if self.path == '/merchant/signup':

            # Return the list of accounts
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(merchants).encode())
        else:
            # Invalid endpoint
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Invalid endpoint')
