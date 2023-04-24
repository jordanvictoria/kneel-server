import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
from views import get_all_orders, get_single_order, update_order, create_order, delete_order, get_single_metal, get_all_metals, update_metal



class HandleRequests(BaseHTTPRequestHandler):
    """Controls the functionality of any GET, PUT, POST, DELETE requests to the server
    """
    
    def parse_url(self, path):
        """PARSE."""
        url_components = urlparse(path)
        path_params = url_components.path.strip("/").split("/")
        query_params = []

        if url_components.query != '':
            query_params = url_components.query.split("&")

        resource = path_params[0]
        id = None

        try:
            id = int(path_params[1])
        except IndexError:
            pass  # No route parameter exists: /animals
        except ValueError:
            pass  # Request had trailing slash: /animals/

        return (resource, id, query_params)

    def do_GET(self):
        """GET."""
        self._set_headers(200)

        response = {}

        parsed = self.parse_url(self.path)

        if '?' not in self.path:
            ( resource, id, query_params ) = parsed

            if resource == "orders":
                if id is not None:
                    response = get_single_order(id)
                else:
                    response = get_all_orders()

            if resource == "metals":
                if id is not None:
                    response = get_single_metal(id)
                else:
                    response = get_all_metals(query_params)

        else:
            (resource, id, query_params ) = parsed

            if resource == 'metals':
                response = get_all_metals(query_params)

        self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        """Handles POST requests to the server"""

        
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)
        ( resource, id, query_params ) = self.parse_url(self.path)     
        response = None

        
        if resource == "orders":
            response = create_order(post_body)

        self.wfile.write(json.dumps(response).encode())

    def do_PUT(self):
        """Handles PUT requests to the server"""
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        ( resource, id, query_params ) = self.parse_url(self.path)

        success = False

        if resource == "orders":
            success = update_order(id, post_body)

        if resource == "metals":
            success = update_metal(id, post_body)

        if success:
            self._set_headers(204)
        else:
            self._set_headers(404)

        self.wfile.write("".encode())

    def _set_headers(self, status):
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
    def do_DELETE(self):
        """Handles DELETE requests to the server"""
        self._set_headers(204)

        ( resource, id, query_params ) = self.parse_url(self.path)

        if resource == "orders":
            delete_order(id)

        self.wfile.write("".encode())

    def do_OPTIONS(self):
        """Sets the options headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type, Accept')
        self.end_headers()



def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
