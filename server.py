# import json
# from http.server import BaseHTTPRequestHandler, HTTPServer
# from urllib.parse import urlparse
# from repository import all, retrieve, create, update, delete


# class HandleRequests(BaseHTTPRequestHandler):
#     """Controls the functionality of any GET, PUT, POST, DELETE requests to the server
#     """

#     # Replace existing function with this
#     def parse_url(self, path):
#         url_components = urlparse(path)
#         path_params = url_components.path.strip("/").split("/")
#         query_params = url_components.query.split("&")
#         # query_params = url_components.query
#         resource = path_params[0]
#         id = None

#         try:
#             id = int(path_params[1])
#         except IndexError:
#             pass
#         except ValueError:
#             pass
#         print (url_components)
#         return (resource, id, query_params)

#     def do_GET(self):
#         """Handles GET requests to the server
#         """
#         response = None

#         (resource, id, query_params) = self.parse_url(self.path)

#         if id is not None:
#             if resource == "orders":
#                 response = retrieve(resource, id)
#                 matching_metal = retrieve("metals", response["metalId"])
#                 matching_style = retrieve("styles", response["styleId"])
#                 matching_size = retrieve("sizes", response["sizeId"])
#                 response["price"] = matching_metal["price"] + matching_size["price"] + matching_style["price"]
#                 if query_params[0] == "metal":
#                     response["metal"] = matching_metal
#                 if query_params[0] == "style":
#                     response["style"] = matching_style
#                 if query_params[0] == "size":
#                     response["size"] = matching_size
#             else:
#                 response = retrieve(resource, id)

#             if response is not None:
#                 self._set_headers(200)
#             else:
#                 self._set_headers(404)
#                 response = ''

#         else:
#             self._set_headers(200)
#             response = all(resource)
#         self.wfile.write(json.dumps(response).encode())

#     def do_POST(self):
#         """Handles POST requests to the server"""


#         self._set_headers(201)

#         content_len = int(self.headers.get('content-length', 0))
#         post_body = self.rfile.read(content_len)


#         post_body = json.loads(post_body)


#         (resource, id) = self.parse_url(self.path)


#         new_post = None

#         if resource == "orders":
#             if "metalId" in post_body and "sizeId" in post_body and "styleId" in post_body:
#                 self._set_headers(201)
#                 new_post = create(resource, post_body)
#             else:
#                 self._set_headers(400)
#                 new_post = {
#                 "message": f'{"metalId is required" if "metalId" not in post_body else ""} {"sizeId is required" if "sizeId" not in post_body else ""} {"styleId is required" if "styleId" not in post_body else ""}'
#                 }
#         else:
#             self._set_headers(405)
#             new_post = { "message": "Item cannot be created." }

#         self.wfile.write(json.dumps(new_post).encode())
#     def do_DELETE(self):
#         """Handles DELETE requests to the server"""

        
#         self._set_headers(405)
#         (resource, id) = self.parse_url(self.path)
#         response = { "message": "Deleting this item requires contacting the company directly." }
        

#         self.wfile.write(json.dumps(response).encode())

#     def do_PUT(self):
#         """Handles PUT requests to the server"""
#         content_len = int(self.headers.get('content-length', 0))
#         post_body = self.rfile.read(content_len)
#         post_body = json.loads(post_body)

#         response = {}
#         (resource, id) = self.parse_url(self.path)

#         if resource == "metals":
#             self._set_headers(204)
#             update(resource, id, post_body)
#             response = ""
#         else:
#             self._set_headers(405)
#             response = { "message": "Updating this item requires contacting the company directly." }

#         self.wfile.write(json.dumps(response).encode())

#     def _set_headers(self, status):
#         """Sets the status code, Content-Type and Access-Control-Allow-Origin
#         headers on the response

#         Args:
#             status (number): the status code to return to the front end
#         """
#         self.send_response(status)
#         self.send_header('Content-type', 'application/json')
#         self.send_header('Access-Control-Allow-Origin', '*')
#         self.end_headers()

#     def do_OPTIONS(self):
#         """Sets the options headers
#         """
#         self.send_response(200)
#         self.send_header('Access-Control-Allow-Origin', '*')
#         self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
#         self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type, Accept')
#         self.end_headers()




# def main():
#     """Starts the server on port 8088 using the HandleRequests class
#     """
#     host = ''
#     port = 8088
#     HTTPServer((host, port), HandleRequests).serve_forever()


# if __name__ == "__main__":
#     main()
