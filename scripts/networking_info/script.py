import sys, subprocess

def ping(host):
    """
    Realiza um ping para o host especificado
    """
    try:
        result = subprocess.run(["ping", "-c", "4", host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except Exception as e:
        return f"Erro ao executar o ping: {e}"
    

def traceroute(host):
    """
    Realiza o Traceroute para o host especificado
    """
    try:
        result = subprocess.run(["traceroute", host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except Exception as e:
        return f"Erro ao executar o traceroute: {e}"
    
def whois(domain):
    """
    Obtém informações WHOIS para o domínio especificado
    """
    try:
        result = subprocess.run(["whois", domain], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except Exception as e:
        return f"Erro ao executar o WHOIS: {e}"
    
def dig(domain):
    """
    Realiza a consulta DNS (dig) para o domínio especificado.
    """
    try:
        result = subprocess.run(["dig", domain], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except Exception as e:
        return f"Erro ao executar o Dig: {e}"
    

def main():
    if len(sys.argv) < 2:
        print("Uso: script.py <comando> <argumento>")
        sys.exit(1)

    command = sys.argv[1]
    argument = sys.argv[2]

    if command == "ping":
        print(ping(argument))
    elif command == "traceroute":
        print(traceroute(argument))
    elif command == "whois":
        print(whois(argument))
    elif command == "dig":
        print(dig(argument))
    else:
        print("Comando inválido. Use 'ping', 'traceroute', 'whous' ou 'dig'")
    

if __name__ == "__main__":
    main()