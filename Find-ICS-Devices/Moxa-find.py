# 20/1/2023 Sulaiman Alhasawi
# If you dont have moxa-enum.nse , get it from my GitHub (address)


import nmap

nm = nmap.PortScanner()

nm.scan('ip-addrr', '4800', arguments='-sV --script moxa-enum')

for host in nm.all_hosts():
    print('Host : %s (%s)' % (host, nm[host].hostname()))
    for proto in nm[host].all_protocols():
        lport = nm[host][proto].keys()
        for port in lport:
            if 'moxa' in nm[host][proto][port]['name']:
                print('port : %s\tstate : %s\tservice : %s' % (port, nm[host][proto][port]['state'], nm[host][proto][port]['name']))
