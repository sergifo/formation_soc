#exercice 1
#import nmap

# def simple_port_scan(target, port):
#     nm = nmap.PortScanner()
#     nm.scan("10.125.26.56", "21-443")
#     for host in nm.all_hosts():
#         print('Host : %s (%s)' % (host , nm[host].hostname()))
#         print('State :  %s' % nm[host].state())
#         for proto in nm[host].all_protocols():
#             print('-------------------')
#             print('Protocol : %s' % proto)
#             lport = nm[host][proto].keys()
#             for port in sorted(lport):
#                 print('port : %\tstate : %s' % (port, nm[host][port]['state']))




import nmap
def simple_port_scan(target, ports):
    nm = nmap.PortScanner()
    nm.scan(target, ports)
    for host in nm.all_hosts():
        print('Host : %s (%s)' % (host, nm[host].hostname()))
        print('State : %s' % nm[host].state())
        for proto in nm[host].all_protocols():
            print('----------')
            print('Protocol : %s' % proto)
            lport = nm[host][proto].keys()
            for port in sorted(lport):
                print('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))






            
