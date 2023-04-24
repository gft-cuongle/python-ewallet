from http.server import BaseHTTPRequestHandler


def send_success_response(self: BaseHTTPRequestHandler, status_code, data):
    self.send_response(status_code)
    self.send_header('Content-type', 'application/json')
    self.end_headers()
    self.wfile.write(data)


def send_failure_response(self: BaseHTTPRequestHandler, status_code, data):
    print("Exception: ", status_code, data)
    self.send_response(status_code)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(data)
