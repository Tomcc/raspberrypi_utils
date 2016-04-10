import http.server
import socketserver
import os
import simplejson
import codecs

class HTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
	def __init__(self, request, client_address, server):
		super().__init__(request, client_address, server)


	def do_GET(self):
		print("DO GET")
		return super().do_GET()

	def do_POST(self):    
		requestBytes = self.rfile.read(int(self.headers['Content-Length']))
		req = simplejson.loads(requestBytes)

		if req["command"] == "tv_off":
			print("SHUT OFF TV")
		if req["command"] == "tv_on":
			print("SHUT OFF TV")
		if req["command"] == "scan_music":
			print("SHUT OFF TV")
		if req["command"] == "start_synergy":
			print("SHUT OFF TV")
		else:
			print("Command not recognized")

		return super().do_GET()


PORT = 23453

os.chdir(os.path.dirname(os.path.realpath(__file__)))

Handler = HTTPRequestHandler

httpd = socketserver.TCPServer(("", PORT), Handler)

print("serving at port", PORT)
httpd.serve_forever()