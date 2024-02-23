import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    print("Client TCP")
    client.connect(("127.0.0.1", 4466))
    client.send(b"Oi tudo bem?\n")
    pacotes_recebidos = client.recv(1024).decode()
    print(pacotes_recebidos)
except:
    print("Erro ocorreu...")