'''
Tuplas:
-- uma coleção ordenada e IMUTÁVEL
-- semelhante a lista, porém não pode ser modificada após a criação
'''

import subprocess, sys

# Função para obter informações dos usuários do linux e inserir em uma tupla
def obter_info_usuarios():
    # Executa o comando 'cat /etc/passwd' para obter informações do usuário
    resultado = subprocess.run(['cat', '/etc/passwd'], capture_output=True, text=True)
    saida = resultado.stdout.splitlines()

    # Inicializar lista para armazenar informações dos usuários
    usuarios_info = []

    # Processar cada linha do comando e extrair informações dos usuários
    for linha in saida:
        campos = linha.split(":")
        if len(campos) >= 6:
            nome_usuario = campos[0]
            uid = campos[2]
            diretorio = campos[5]
            usuarios_info.append((nome_usuario, uid, diretorio))
    
    return tuple(usuarios_info)

# Gravar informações no arquivo
def gravar_em_arquivo(info_usuarios, nome_arquivo):
    with open(nome_arquivo, "w") as arquivo:
        for usuario in info_usuarios:
            arquivo.write(f"Nome do usuário: {usuario[0]}, UID: {usuario[1]}, Diretório: {usuario[2]}\n")

# Verificar se o nome do arquivo foi passado como argumento:
if len(sys.argv) != 2:
    print("Uso: python3 tuplas.py <nome_do_arquivo.txt>")
    sys.exit(1)

# Obter informações dos usuários do sistema
usuarios_linux = obter_info_usuarios()

# Gravar informações dos usuários no arquivo especificado
nome_arquivo = sys.argv[1]
gravar_em_arquivo(usuarios_linux, nome_arquivo)

# Exibir informações dos usuários
for usuario in usuarios_linux:
    print(f"Nome do usuário: {usuario[0]}, UID: {usuario[1]}, Diretório: {usuario[2]}")