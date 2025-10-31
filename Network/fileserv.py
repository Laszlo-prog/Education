import socket
host = 'localhost'
port = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
print("The server is running and waiting for connections...")
comm, address =s.accept()
try:
    fileName = comm.recv(1024).decode('utf-8')
    file = open(fileName, 'rb')
    readFile = file.read(1024)
    comm.send(readFile)
    file.close()
except FileNotFoundError:
    comm.send(b'File not found')
    

comm.close()
