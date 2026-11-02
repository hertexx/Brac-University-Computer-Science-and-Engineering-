import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 5002))
server.listen(1)

conn, addr = server.accept()
message = conn.recv(1024).decode()

vowels = "aeiouAEIOU"
count = sum(1 for c in message if c in vowels)

if count == 0:
    reply = "Not enough vowels"
elif count <= 2:
    reply = "Enough vowels I guess"
else:
    reply = "Too many vowels"

conn.send(reply.encode())
conn.close()
server.close()
