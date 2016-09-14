import socket

#allocate a new socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#listen on port 8000
server.bind(('0.0.0.0', 8000))
server.listen(1)

print "Waiting for connections..."
client, address = server.accept()
print "Connected!"
print address

