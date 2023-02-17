import socket

# Create a socket object
server_socket = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

# Get local machine name
hostname = socket.gethostname()
port = 444

server_socket.bind((hostname, port))

server_socket.listen(3)

print(f'server running on port {port} and hostname {hostname}')
print(f'Ip adress is {socket.gethostbyname(hostname)}')
while True:
    client_socket, address = server_socket.accept()
    print(f'Connection sucessul from {address}')

    message = 'Thank you for connection in my server'
    client_socket.send(message.encode('ascii'))
    # Close connection
    client_socket.close()