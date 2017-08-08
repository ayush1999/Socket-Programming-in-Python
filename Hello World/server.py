import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host= socket.gethostname()
port=12345

s.bind((host,port))
s.listen(5)
c,addr=s.accept()
c.send(b'Hello World!')
c.close()
