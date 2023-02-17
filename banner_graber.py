import socket


def main():
    ip_address = str(input('target ip addres: '))
    port = int(input('target port: '))
    print(f'ip address is {ip_address} and port is {port}')
    banner_graber(ip_address, port)


def banner_graber(ip_address, port):
    socket_banner = socket.socket()
    socket_banner.connect((ip_address, port))
    receive = socket_banner.recv(1024)

    print(f'message is {receive.decode("ascii")}')


if __name__ == '__main__':
    main()