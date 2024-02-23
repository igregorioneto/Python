import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    IP = input("Digite o IP para conexão com o servicor: ")
    PORT = int(input("Digite a PORT para a conexão com o servidor: "))
    print("Iniciando chat...")
    while True:
        msg = input("Mensagem: ") + "\n"
        if msg == "sair\n":
            break
        client.sendto(msg.encode(), (IP, PORT))
        data, sender = client.recvfrom(1024)
        ip, port = sender
        msg = data.decode()
        if msg == "sair\n":
            break
        print(f"{ip} : {msg}")

except Exception as e:
    print(f"Erro aconteceu: {e}")
finally:
    client.close()
