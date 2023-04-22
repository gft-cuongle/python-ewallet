from http.server import BaseHTTPRequestHandler
from app.service import merchant_service
import json


class MerchantController(BaseHTTPRequestHandler):

    def do_POST(self):
        """
        Handles POST requests
        """
        if self.path == '/merchant/signup':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            merchant_data = json.loads(post_data.decode())
            merchant_name = merchant_data.get('merchantName')
            merchant_url = merchant_data.get('merchantUrl')
            if merchant_name is None:
                self.send_response(400)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(b'Merchant name is mandatory')
                return
            if merchant_url is None:
                self.send_response(400)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(b'Merchant url is mandatory')
                return

            merchant = merchant_service.create_merchant(merchant_name, merchant_url)

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(merchant).encode())
        else:
            # Invalid endpoint
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Invalid endpoint')
