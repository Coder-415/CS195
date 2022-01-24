#Web Service Homework
#Due Date: 11/1/2020


#Task: 
#Write an HTTP service that dynamically acquires a port number 
#and serves a single copy of a memorable text to the first request 
#that comes in. Because of firewall rules, requests to services on 
#high ports running on hills have to come from within the college network


import http.server
#from urllib.parse import urlparse
#import urllib.request, sys
import socket

def findport():
	s = socket.socket()
	s.bind(('',0))
	port_num  = s.getsockname()[1]
	s.close()
	return port_num

#Create the handler class to respond to requests 
class Handler(http.server.BaseHTTPRequestHandler):
	def do_GET(self):
	#200 is the http status code for "OK" -- request succeeded:
		self.send_response(200)
		#Our handler will respond to a request in plain text
		self.send_header('Content-Type','text/plain')
		self.end_headers()
		#Write a file that says 'Hello!' in response to a request:
		self.address_string()
		self.wfile.write('Hello, thank you for submitting!\n'.encode())

if __name__ == '__main__':
	server = ('',findport()) #(host,port_number)
	print("Serving at port:", server[1],"-- Press CRTL + C to terminate")
	print("\nTo test, launch a separate terminal window and SSH session and \n either type or copy paste 'curl http://localhost:",server[1],"'",sep='')
	#Initiate the Handler class:
	httpd = http.server.HTTPServer(server,Handler)
	#Activate the server and serve continuously:
	httpd.serve_forever()

