from http.server import BaseHTTPRequestHandler
from random_address import real_random_address_by_state
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Extract the state query parameter
        path = self.path
        if '?' in path:
            query = path.split('?',1)[1]
            state = query.split('=')[1]
            address = real_random_address_by_state(state)
        else:
            address = {"error": "State abbreviation is required as a query parameter."}

        # Write response
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(address).encode())