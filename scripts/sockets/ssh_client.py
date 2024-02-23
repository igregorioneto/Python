import paramiko

host = "127.0.0.1"
user = "user"
password = "pass"

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=user, password=password)

while True:
    stdin, stdout, stderr = client.exec_command(input("Comando: "))
    for line in stdout.readlines():
        print(line.strip())

    erros = stderr.readlines()
    if erros:
        print(erros)
