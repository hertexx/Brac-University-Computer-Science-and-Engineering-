import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 5002))

msg = input("Enter a message: ")
client.send(msg.encode())

reply = client.recv(1024).decode()
print("Server says:", reply)

client.close()
