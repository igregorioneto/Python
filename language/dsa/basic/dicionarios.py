'''
Dicionários:
-- coleção não ordenada de chave e valor
-- os elementos de um dicionários são acessados por suas chaves em vez de indices.
'''
import sys, json

def carregar_json(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        dados = json.load(arquivo)
    return dados

try:
    arquivo = sys.argv[1]

    print("Listando Dispositivos de Rede:")    
    
    #Exemplo sem precisar utilizar o arquivo
    '''    
    dispositivos_rede = {
        "router": {"ip": "192.168.1.1", "porta": 22, "protocolo": "SSH"},
        "switch": {"ip": "192.168.1.2", "porta": 23, "protocolo": "Telnet"}
    }
    '''

    # Exemplo de dicionário contendo informações de dispositivos de rede:
    dispositivos_rede = carregar_json(arquivo)

    '''
    Caso for um dicionário normal em vez de dispositivos_rede['dispositivos'] ->
    utilizar dispositivos_rede.items()
    '''

    for info in dispositivos_rede['dispositivos']:
        print(f"Dispositivo: {info['nome']}, IP: {info['ip']}, PORTA: {info['porta']}, PROTOCOLO: {info['protocolo']}")
except:
    print("Uso: python3 dicionarios.py arquivo.json")


