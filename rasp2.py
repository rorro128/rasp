from time import sleep
import nmap

nm = nmap.PortScanner()
nm.scan('192.168.1.0/24', arguments="-T4 -F")

for host in nm.all_hosts():
    print(f"IP: " + nm[f"{host}"]['addresses']['ipv4'] )
    for proto in nm[host].all_protocols():
        print('Protocol : %s' % proto)
        lport = nm[host][proto].keys()
        for port in lport:
            print ('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))