"""websocketserver:
"""

# from: http://sidekick.windforwings.com/2013/03/minimal-websocket-broadcast-server-in.html

import socket, hashlib, base64, threading
import json

import errno

class WebsocketClient:
	MAGIC = '258EAFA5-E914-47DA-95CA-C5AB0DC85B11'
	HSHAKE_RESP = "HTTP/1.1 101 Switching Protocols\r\n" + \
							"Upgrade: websocket\r\n" + \
							"Connection: Upgrade\r\n" + \
							"Sec-WebSocket-Accept: %s\r\n" + \
							"\r\n"

	def __init__(self, engine, connection, address):
		self.connection = connection
		self.address = address
		self.engine = engine
		self.handshaked = False

	def serve_connection(self):
		if (self.handshaked == False):
			self.handshaked = self.handshake()
			return True
		else:
			return self.poll_message()

	def send(self, data):
		# 1st byte: fin bit set. text frame bits set.
		# 2nd byte: no mask. length set in 1 byte. 
		resp = bytearray([0b10000001, len(data)])
		# append the data bytes
		for d in bytearray(data):
			resp.append(d)
		try:
			self.connection.send(resp)
			return True
		except socket.error, e:
			self.engine.log('send: socket error' + str(e))
		except Exception as e:
			self.engine.log("send: Exception %s" % (str(e)))
			return False

	def poll_message(self):
		try:
			data = self.recv_data()
			#self.engine.log("received: %s" % (data,))
			#self.broadcast_resp(data)
			try:
				message = json.loads(data)
			except ValueError, e:
				self.engine.log("invalid json")
				self.send('invalid json')
			else:
				if ('type' in message) and ('content' in message) and (message['type'] == 'message'):
					if message['content'] == 'pressed':
						self.engine.log("websocket received pressed")
						self.engine.callPythonKeyPressed(EngineModule.Keys.K_SPACE)
						self.send('received pressed')
					elif message['content'] == 'released':
						self.engine.log("websocket received released")
						self.engine.callPythonKeyReleased(EngineModule.Keys.K_SPACE)
						self.send('received released')
					else:
						self.send('received: unknown content')
				else:
					self.send('received: unknown type')
			return True
		except socket.error, e:
			if e.errno == errno.EAGAIN:
				#self.engine.log('errno.EAGAIN')
				pass
			else:
				#self.engine.log('poll_message: socket error' + str(e))
				pass
			pass
		except Exception as e:
			pass
			self.engine.log("poll_message: Exception %s" % (str(e)))
			return False

	def recv_data(self):
		# as a simple server, we expect to receive:
		#		- all data at one go and one frame
		#		- one frame at a time
		#		- text protocol
		#		- no ping pong messages
		data = bytearray(self.connection.recv(512))
		if(len(data) < 6):
			raise Exception("Error reading data")
		# FIN bit must be set to indicate end of frame
		assert(0x1 == (0xFF & data[0]) >> 7)
		# data must be a text frame
		# 0x8 (close connection) is handled with assertion failure
		assert(0x1 == (0xF & data[0]))
		# assert that data is masked
		assert(0x1 == (0xFF & data[1]) >> 7)
		datalen = (0x7F & data[1])
		#self.engine.log("received data len %d" %(datalen,))
		str_data = ''
		if(datalen > 0):
			mask_key = data[2:6]
			masked_data = data[6:(6+datalen)]
			unmasked_data = [masked_data[i] ^ mask_key[i%4] for i in range(len(masked_data))]
			str_data = str(bytearray(unmasked_data))
		return str_data

	def parse_headers (self, data):
		headers = {}
		lines = data.splitlines()
		for l in lines:
				parts = l.split(": ", 1)
				if len(parts) == 2:
						headers[parts[0]] = parts[1]
		headers['code'] = lines[len(lines) - 1]
		return headers

	def handshake (self):
		try:
			data = self.connection.recv(2048)
			#self.engine.log('Handshaking...')
			headers = self.parse_headers(data)
			#self.engine.log('Got headers:')
			#for k, v in headers.iteritems():
			#		self.engine.log k, ':', v
			key = headers['Sec-WebSocket-Key']
			resp_data = self.HSHAKE_RESP % ((base64.b64encode(hashlib.sha1(key+self.MAGIC).digest()),))
			#self.engine.log('Response: [%s]' % (resp_data,))
			#return self.connection.send(resp_data)
			self.engine.log('Handshaked')
			self.connection.send(resp_data)
			return True
		except socket.error, e:
			self.engine.log('handshake: socket error' + str(e))
			pass
		return False

class PollingWebSocketServer:
	server_socket = None
	address = ''
	connected_clients = []

	def __init__(self, engine, port=4545):
		self.port = port
		self.server_init()
		self.engine = engine

	def server_init(self):
		if (self.server_socket == None):
			self.server_socket = socket.socket()
			self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			self.server_socket.setblocking(0)
			#server_socket.settimeout(1)
			self.server_socket.bind((self.address, self.port))
			self.server_socket.listen(5)

	def poll_connections(self):
		try:
			conn, addr = self.server_socket.accept()
			self.connected_clients.append(WebsocketClient(self.engine,conn,addr))
		except socket.error, e:
			#self.engine.log('poll_connections: socket error' + str(e))
			pass

		connections_to_remove = []
		for c in self.connected_clients:
			if (c.serve_connection() == False):
				connections_to_remove.append(c)
		for c in connections_to_remove:
			self.connected_clients.remove(c)

def init(Engine,EngineModule,objects):
	try:
		objects.get()["websocket"] = PollingWebSocketServer(Engine)
		objects.setUnsavable("websocket")
	except Exception as e:
		Engine.log("websocket server init: Exception %s" % (str(e)))
		Engine.quit()

def guiUpdate(Engine,EngineModule,selection,objects):
	if "websocket" in objects.get():
		ws = objects.get()["websocket"]
		try:
			ws.poll_connections()
		except Exception as e:
			Engine.log("websocket guiUpdate poll_connections: Exception %s" % (str(e)))

