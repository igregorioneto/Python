import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

file = open("output.txt", "w")

try:
    server.bind(("0.0.0.0", 4466))
    server.listen(5)
    print("Listening...")

    client_socket, address = server.accept()
    ip, port = address
    print(f"Received from: [ {ip} ]")

    while True:
        data = client_socket.recv(1024).decode()
        if data == "senhasecreta\n":
            print("Desconectando...")
            break
        file.write(data)

except Exception as e:
    print(f"Error: {e}")
finally:
    server.close()
