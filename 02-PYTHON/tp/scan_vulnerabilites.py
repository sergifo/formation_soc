import nmap
rm = nmap.PortScanner()
import os
import vulners

targets = {
    'DVWA' : os.getenv("DVWA_IP")
}

vulners_api = vulners.Vulners(api_key=os.getenv("VULNERS_KEY"))

def save_results(results, filename="scan-results/scan_results.txt"):
    with open (filename, "a") as file:
        file.write(results + "\n")

def search_vulnerability(service_name):
    search_query = f"type:cve and affectedsoftware.name {service_name}"
    results = vulners_api.search(query=search_query)
    vulnerabilities = []
    if results:
        for result in results:
            cvss_score = result.get("cvss", {}).get("score", 0)
            vulnerabilities.append((cvss_score, f"-{result['id']}"))
        #SSort vulnerabilities by CVSS score in descending order
        vulnerabilities.sort(reverse=True, key=lambda x: x[0])
        output = f"Vulnerabilities found for {service_name} (sorted by CVSS):\n" + "\n".join(v[1] for v in vulnerabilities)
    else:
        output = f"No know vulnerabilities found for {service_name}.\n"
        print(output)
        save_results(output)


def scan_hosts():
    for name, ip in targets.items():
        print(f"Scanning {name} at {ip}")
        nm.scan(ip, '1-65535', '-sV')  
        for host in nm.all_hosts():
            print('----------------------------------------------------')
            print('Host : %s (%s)' % (host, nm[host].hostname()))
            print('State : %s' % nm[host].state())
            for proto in nm[host].all_protocols():
                print('----------')
                print('Protocol : %s' % proto)
                lport = nm[host][proto].keys()
                for port in sorted(lport):
                    service = nm[host][proto][port]['name']
                    print('Port : %s\tService: %s' % (port, service))
                    search_vulnerability(service_name=service)


scan_hosts()
            
