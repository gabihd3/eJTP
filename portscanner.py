import socket
import re

dest_ip = input('Whats the IP?')
port_range = input('Whats the port range?')

ports = re.findall('\d{1,5}', port_range)
lowport = int(ports[0])
highport = int(ports[-1])

print(dest_ip,'checking between ports',  lowport, 'and', highport)

for i in range(highport-lowport):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    status = s.connect_ex((dest_ip,i))
    if status == 0:
        print(i,'open')
    elif status == 1:
        print(i,'closed')
    else:
        print(status)
    s.close()