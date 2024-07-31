import nmap
import vulners
import os
import json



vulners_api = vulners.Vulners(api_key=os.environ.get("VULNERS_KEY"))

def save_vulnerabilities(service, vulnerability):
    with open(f"{service}.json", 'w') as file:
        json.dump(vulnerability, file, indent=4)

def nmap_scan(target_ip, ports='8080,3306,80,3000'):
    scanner = nmap.PortScanner()
    scanner.scan(target_ip, ports, arguments='-sV')
    return scanner


def check_vulnerabilities(nmap_scanner):
    print("En cours de scan : ......")
    for host in nmap_scanner.all_hosts():
        for protocol in nmap_scanner[host].all_protocols():
            liste_ports = nmap_scanner[host][protocol].keys()
            for port in liste_ports:
                service_info = nmap_scanner[host][protocol][port]
                print(f"Port : {port}/{protocol}")
                print(f"Service : {service_info['name']}")
                print(f"Version du Service : {service_info['product']}, {service_info['version']}")
                if service_info['product'] and service_info['version']:
                    query = f"{service_info['product']} {service_info['version']}"
                    result_analys = vulners_api.search(query=query)
                    for vulnerability in result_analys:
                        save_vulnerabilities(service_info['name'], vulnerability=vulnerability)
                        print(f"{vulnerability['id']}  {vulnerability['title']}")

def main():
    target = "10.125.26.56"
    scanner = nmap_scan(target_ip=target)
    check_vulnerabilities(scanner)

main()