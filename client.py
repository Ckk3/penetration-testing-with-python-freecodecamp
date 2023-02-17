import socket

client_socket = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

hostname = socket.gethostname()
port = 444

print(f'connecting to server on port {port} and hostname {hostname}')
client_socket.connect((hostname, port))
# Receive data from server with 1024 bytes limit
message = client_socket.recv(1024)

# Close connection
client_socket.close()

print(f'message receiveid is {message.decode("ascii")}')