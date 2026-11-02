import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 5001))
server.listen(1)

print("Server is waiting for connection...")

conn, addr = server.accept()
data = conn.recv(1024).decode()

print("Client connected")
print("Received info:", data)

conn.close()
server.close()
