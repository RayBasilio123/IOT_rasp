from multiprocessing.dummy import connection
import requests
import json, os
import subprocess
from getmac import get_mac_address
import getpass



url_pattern ='http://127.0.0.1:5000/'

# r = requests.get(url_pattern+'/get_port?mac_address=1234&nome_dispositivo=rasp2')
# print(r.json())

def request_connection(mac_address, nome_dispositivo):
    r = requests.get(url_pattern+'/get_port?mac_address={}&nome_dispositivo={}'.format(mac_address, nome_dispositivo))
    return r.json()
    
 
def  performs_reverse_tunnel(available_port):
    return subprocess.Popen('test_script.sh {} '.format(str(available_port))) 

def  ssh_tunnel_check(port):
  return os.system('./create_ssh_tunnel.sh {}' .format(str(port)) )
    

def register_device(port):
    r = requests.get(url_pattern+'/register_device?port={}'.format(port))
    return r.json()

def register_password(password,mac_address):
    r = requests.get(url_pattern+'/register_password?password={}&mac_address={}'.format(password,mac_address))
    return r.json()

    
configuration = request_connection(get_mac_address(),getpass.getuser())
print(configuration)
# ssh_tunnel_check(configuration['porta'])
# print(register_device(configuration['porta']))
#print(register_password("3553",configuration['mac_address']))

# performs_reverse_tunnel("oi")
