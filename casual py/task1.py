from requests import get

ip = get('https://api.ipify.org').text
print(f'My public IP address is: {ip}')


import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect(hostname='54.165.97.91', username='ec2-user', password='paramiko123',port=22)
sftp_client = ssh.open_sftp()
# sftp_client.get('/abhijeet/bypass.txt','''localpath''')
print(dir(sftp_client))
sftp_client.close()
ssh.close()


