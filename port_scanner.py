import socket

def main():
    ip_address = str(input('target ip addres: '))
    port = int(input('target port: '))
    print(f'ip address is {ip_address} and port is {port}')
    port_scanner(ip_address, port)

def port_scanner(ip_address, port):
    socket_scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect ex its like connect but do not raise a Exception if the connection fails
    if socket_scanner.connect_ex((ip_address, port)):
        print(f'port {port} is closed')
    else:
        print(f'port {port} is OPEN')

if __name__ == '__main__':
    main()