from http.server import BaseHTTPRequestHandler
from app.service import merchant_service
import json

from app.utils.response_util import send_failure_response, send_success_response


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
                send_failure_response(self, 400, b'Merchant name is mandatory')
                return
            if merchant_url is None:
                send_failure_response(self, 400, b'Merchant url is mandatory')
                return
            merchant = merchant_service.create_merchant(merchant_name, merchant_url)
            send_success_response(self, 200, json.dumps(merchant).encode())
        else:
            # Invalid endpoint
            send_failure_response(self, 404, b'Invalid endpoint')
