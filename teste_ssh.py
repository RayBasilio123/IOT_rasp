import paramiko
import sshtunnel

with sshtunnel.open_tunnel(
    ("ec2-44-192-129-106.compute-1.amazonaws.com", 22),
    ssh_username="ubuntu",
    ssh_pkey=paramiko.SSHKey,

    # ssh_private_key_password="secret",
    remote_bind_address=("127.0.0.1", 22),
    local_bind_address=('0.0.0.0', 10022)
) as tunnel:
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect('127.0.0.1', 10022)
    # do some operations with client session
    client.close()

print('FINISH!')