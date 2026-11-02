import socket
import platform

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 5001))

device_name = platform.node()
ip_address = socket.gethostbyname(socket.gethostname())

message = f"IP: {ip_address}, Device Name: {device_name}"
client.send(message.encode())

client.close()
