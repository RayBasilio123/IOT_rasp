from multiprocessing.dummy import connection
import requests
import json, os
import subprocess
from getmac import get_mac_address
import getpass
import jwt



url_pattern ='http://127.0.0.1:5000/'

# encoded_jwt = jwt.encode({"some": "payload"}, "secret", algorithm="HS256")
# print(encoded_jwt)
# print(jwt.decode(encoded_jwt, "secret", algorithms=["HS256"]))

# r = requests.get(url_pattern+'/get_port?mac_address=1234&nome_dispositivo=rasp2')
# print(r.json())

def request_connection(mac_address, nome_dispositivo):
    r = requests.get(url_pattern+'/get_port?mac_address={}&nome_dispositivo={}'.format(mac_address, nome_dispositivo))
    return r.json()
    
 
def  performs_reverse_tunnel(available_port):
    return subprocess.Popen('test_script.sh {} '.format(str(available_port))) 

def  ssh_tunnel_check(port):
  return os.system('./create_ssh_tunnel.sh {}' .format(str(port)) )
    

def disconect_device(port):
    r = requests.get(url_pattern+'/disconect_device?port={}'.format(port))
    return r.json()

def register_password(password,mac_address):
    r = requests.get(url_pattern+'/register_password?password={}&mac_address={}'.format(password,mac_address))
    return r.json()




def send_password(key, mac_address) :
    encoded_jwt = jwt.encode({"key": key, "mac_address": mac_address}, "secret", algorithm="HS256")
    r = requests.post(url_pattern+'/register_password', json={"package": encoded_jwt})
    return r.json()






configuration = request_connection(get_mac_address(),getpass.getuser())

print(configuration)

send_password(3553,get_mac_address())
ssh_tunnel_check(configuration['porta'])
# print(disconect_device(configuration['porta']))
#print(register_password("3553",configuration['mac_address']))

# performs_reverse_tunnel("oi")
