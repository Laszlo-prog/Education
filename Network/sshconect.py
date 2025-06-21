#A. SSH Automation with paramiko (Basic Example)
import paramiko

# SSH connection setup
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.1.1', username='admin', password='password')

# Execute a command
stdin, stdout, stderr = ssh.exec_command('show ip interface brief')
print(stdout.read().decode())

# Close connection
ssh.close()