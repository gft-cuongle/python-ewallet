import threading
from http.server import HTTPServer
from app.utils import transaction_update_scheduler

from app.controller.routing_request_controller import RoutingRequestHandler

if __name__ == "__main__":
    pass
    print("Cuong-Le Python E-wallet")

    # Set the server address and port number
    server_address = ('', 8000)

    # Create an HTTP server as the request handler
    httpd = HTTPServer(server_address, RoutingRequestHandler)

    http_server_thread = threading.Thread(target=httpd.serve_forever)
    # Start the server
    print('Starting server...')
    http_server_thread.start()

    # Schedule task update the status of expired transaction
    transaction_status_update_thread = threading.Thread(target=transaction_update_scheduler.start_scheduled_task)
    transaction_status_update_thread.start()

    http_server_thread.join()
    transaction_status_update_thread.join()
