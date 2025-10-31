import socket
host = 'localhost'
port = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
print("The server is running and waiting for connections...")
comm, address =s.accept()
message = 'Hello, World!' + "\r\n"
comm.send(message.encode('utf-8'))
comm.close()
