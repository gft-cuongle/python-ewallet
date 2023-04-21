from http.server import HTTPServer

from app.controller.routing_request_controller import RoutingRequestHandler

if __name__ == "__main__":
    pass
    print("Cuong-Le Python E-wallet")

    # Set the server address and port number
    server_address = ('', 8000)

    # Create an HTTP server as the request handler
    httpd = HTTPServer(server_address, RoutingRequestHandler)

    # Start the server
    print('Starting server...')
    httpd.serve_forever()
