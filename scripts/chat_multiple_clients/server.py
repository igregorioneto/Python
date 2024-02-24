import socket
import threading

# Connected Clients
clients = []

# Receive and send messages
def handle_client(client_socket, port):
    while True:
        try:
            data = client_socket.recv(1024).decode()
            if not data:
                break
            
            if data == "exit\n":
                clients.remove(client_socket)

            message_with_port = f"{port}: {data}"
            print(message_with_port)

            # Transmit messages to connected clients
            for c in clients:
                if c != client_socket:
                    c.send(message_with_port.encode())
        except Exception as e:
            print(f"Error receive message: {e}")
            break


try:
    print("===== SERVER =====")
    server_ip = input("Enter server IP: ")
    server_port = int(input("Enter server PORT: "))

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind((server_ip, server_port))
    server.listen(5)
    print("Listening...")
    
    while True:
        client_socket, address = server.accept()
        ip, port = address

        # Add clients to clients list
        clients.append(client_socket)
        
        print(f"Server connect in [{ip}]:{port}")

        # data = client_socket.recv(1024).decode()
        # if data == "exit\n":
        #    break
        
        client_thread = threading.Thread(target=handle_client, args=(client_socket, port))
        client_thread.start()
    
except Exception as e:
    print(f"Error with server: {e}")
finally:
    server.close()
