import rpyc
print("connect to server")
c = rpyc.classic.connect("127.0.0.1",45678)
print(dir(c))


