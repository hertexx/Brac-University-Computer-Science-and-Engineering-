import socket

format = "utf-8"
data =16
port = 5050
disconnected_msg = "off"
hostname = socket.gethostname()

host_addr = socket.gethostbyname(hostname)

server_socket_addr = (host_addr, port)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(server_socket_addr)


def msg_to_send(msg):
    message = msg.encode(format)
    msg_length = len(message)
    send_length = str(msg_length).encode(format)
    send_length += b" "*(data - len(send_length))

    client.send(send_length)
    client.send(message)

    client_recv =client.recv(2048).decode(format)
    print(client_recv)


while True:
    
    msgg = input("Enter how many hours a person works: ")
    msg_to_send(msgg)
    








 
