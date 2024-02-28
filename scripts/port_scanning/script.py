import sys, socket

def scan(host, ports, timeout=0.05):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.timeout(timeout)
        for port in ports:
            code = client.connect_ex((host, port))
            if code == 0:
                print(f"[+] {port} open")
            
    except:
        print("Error, something is wrong.")

if __name__ == "__main__":
    ports = [21,22, 23,25,80,443,445,8080,8443,3306,139,135]
    timeout = 0.05
    if len(sys.argv) >=2:
        host = sys.argv[1]
        if len(sys.argv) >= 3:
            ports = sys.argv[2].split(",")
            if len(sys.args) >= 4:
                timeout = sys.args[3]
        scan(host, ports, timeout)
    else:
        print("Usage: python3 script.py <host> <port,port> <timeout>")
    