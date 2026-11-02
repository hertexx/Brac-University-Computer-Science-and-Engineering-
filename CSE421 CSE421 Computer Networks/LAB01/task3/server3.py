import socket
import threading

def handle_client(conn):
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

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 5003))
server.listen(5)

print("Multi-threaded server running...")

while True:
    conn, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(conn,))
    thread.start()
