import socket
import threading

# Receive messages
def receive_messages(client_socket):
    while True:
        try:
            data = client_socket.recv(1024).decode()
            if not data:
                break
            print(data)
        except Exception as e:
            print(f"Error receive message: {e}")
            break

def main():
    try:
        print("===== CLIENT =====")
        server_ip = input("Enter server IP: ")
        server_port = int(input("Enter server PORT: "))

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_ip, server_port))
        print(f"Connected to server at {server_ip}:{server_port}")

        receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
        receive_thread.start()

        while True:
            message = input("Enter message (type 'exit' to quit): ")
            client_socket.send(message.encode())
            if message == 'exit':
                break

    except Exception as e:
        print(f"Error with client: {e}")
        return
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()