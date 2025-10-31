import socket
host = 'localhost'
port = 8080
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
fileName = test.txt
s.send(fileName.encode('utf-8'))
readFile = s.recv(1024)
comm.send(readFile)
file.close()

s.close()
