import rpyc
from rpyc.utils.server import Server
from rpyc.utils.server import ThreadedServer

import socket

class RpycServer(Server):

	#def __init__(self,):

	def start(self):
		self.listener.listen(self.backlog)
		self.active = True

	def listen(self):
		sock = None
		try:
			sock, addrinfo = self.listener.accept()
		except socket.timeout:
			pass
		except socket.error:
			pass
		#else: 
		#break
		if sock:
			sock.setblocking(False)
			self.clients.add(sock)
			self._accept_method(sock)
			

	def _accept_method(self,sock):
		self._authenticate_and_serve_client(sock)

aa = "hello"
def greet():
	print("hi")

t = ThreadedServer(rpyc.core.SlaveService,hostname="127.0.0.1",port=45678)
print("starting server")
t.logger.quiet = "quiet"
t.start()


"""
r = RpycServer(rpyc.core.SlaveService,hostname="127.0.0.1",port=45678,protocol_config = {"allow_public_attrs" : True})
print("starting server")
r.start()
while True:
	r.listen()
"""
