import os
import paramiko
from file_utils.get_config import get_config


host_aws = get_config()['Server']['host_aws'] or os.environ.get('host_aws')
port_aws = int(get_config()['Server']['port_aws'])
username_aws = get_config()['Server']['username_aws']
password_aws = get_config()['Server']['password_aws'] or os.environ.get('password_aws')

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(host_aws, port=port_aws, username=username_aws, password=password_aws)
