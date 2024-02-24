import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    print("===== SERVER =====")
    server.bind(("0.0.0.0", 4422))
    server.listen(5)
    print("Listening...")

    client_socket, address = server.accept()
    ip, port = address
    print(f"Server connect in [{ip}]:{port}")
    
    while True:
        data = client_socket.recv(1024).decode()
        if data == "exit\n":
            break
        
except Exception as e:
    print(f"Error with server: {e}")
finally:
    server.close()
