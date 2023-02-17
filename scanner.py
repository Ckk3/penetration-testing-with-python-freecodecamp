import nmap

scanner = nmap.PortScanner()

print("Welcome, this is a simple nmap automation tool for studies only")
print(f'Nmap version: {scanner.nmap_version()}')
print('-=' * 30)

ip_address = str(input('target ip addres: '))
print(f'ip address is {ip_address}')

print('''
Choose the type of scan you want to run
1 SYN ACK Scan
2 UDP Scan
3 Comprehensive Scan
''')
option = str(input('Enter your option: ')).strip()
print(f'you choose option {option}')


if option == '1':
    scanner.scan(ip_address, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print(f'Ip status: {scanner[ip_address].state()}')
    print(scanner[ip_address].all_protocols())
    print(f'Open tcp ports: {scanner[ip_address]["tcp"].keys()}')
elif option == '2':
    scanner.scan(ip_address, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    print(f'Ip status: {scanner[ip_address].state()}')
    print(scanner[ip_address].all_protocols())
    print(f'Open udp ports: {scanner[ip_address]["udp"].keys()}')
elif option == '3':
    scanner.scan(ip_address, '1-1024', '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print(f'Ip status: {scanner[ip_address].state()}')
    print(scanner[ip_address].all_protocols())
    print(f'Open tcp ports: {scanner[ip_address]["tcp"].keys()}')
else:
    print('Invalid option')