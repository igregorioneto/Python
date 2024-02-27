'''
Conjuntos:
-- coleção não ordenada e sem elementos duplicados
-- suporta operações como união, interseção e diferença
'''
import sys

def carregar_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        dados = arquivo.read()
    return dados

try:
    arquivo = sys.argv[1]
    # Exemplo de conjuntos com IP suspeitos
    enderecos_suspeitos = {"192.168.1.100", "10.0.0.1", "172.16.0.1"}

    # Logs de acesso a um servidor web
    '''
    logs = ["192.168.1.100 - - [25/Feb/2024:12:00:00] GET /index.html HTTP/1.1",
            "10.0.0.1 - - [25/Feb/2024:12:05:00] POST /login.php HTTP/1.1",
            "192.168.1.101 - - [25/Feb/2024:12:10:00] GET /admin HTTP/1.1"]
    '''
    logs = carregar_arquivo(arquivo).split()

    enderecos_identificados = set()
    for log in logs:
        if log in enderecos_suspeitos:
            enderecos_identificados.add(log)

    #print("Endereços IP associados a solicitações suspeitas: ")
    for endereco in enderecos_identificados:
        print(endereco)
except:
    print("Uso: python3 conjuntos.py logs.txt")
    pass