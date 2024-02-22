import sys
import os
from fabric import Connection
import tarfile
import shutil
from datetime import datetime

'''
    1- Criar um diretório na pasta do usuário para receber backup:
    Ex. meus_documentos

    2 -Criar arquivos de testes:
    Ex. word1.txt, word2.txt

    3 - Criar uma pasta chamada backup

    4 - Criar um arquivo chamado backup.sh com shell,
    da permissões de execução para este arquivo.

    5 - Copiar todos os arquivos do diretório meus_documentos
    para backup e adicionar a data atual:
    Ex. backup_2024-02-21.tar.gz
'''

def backup_dir(userdir, backup_dir_name, dir_for_backup):
    # Verifica sistema linux
    if sys.platform.startswith('linux'):
        #Vai para o diretório Home
        print("Iniciando o backup...")
        os.chdir("/home")
        # Lista as pastas dos arquivos Home
        users = os.listdir("/home")
        # Verifica se a pasta do usuário existe
        if userdir in users:
            # Entra na pasta usuário
            os.chdir(userdir)
            # Lista novamente os diretórios
            directories = os.listdir("./")
            print(directories)
            if dir_for_backup not in directories:
                print(f"Diretório {dir_for_backup} para backup não existe...")
            else:
                # Verifica se a pasta de backup existe, caso não exista é criada
                if backup_dir_name in directories:
                    print(f"Diretório {backup_dir_name} existe...")
                else:
                    os.mkdir(backup_dir_name)
                    print(f"Criando pasta de {backup_dir_name}")
                
                # Listando diretorios novamente
                directories = os.listdir("./")
                print(directories)

                # Entra na pasta para realizar backup dos arquivos
                os.chdir(dir_for_backup)    
                directories = os.listdir("./")
                print(f"Arquivos para backup: {directories}")

                # Cria o nome do arquivo para backup com a data atual
                date_today = datetime.now().strftime("%Y-%m-%d")
                backup_filename = f"backup_{date_today}.tar.gz"

                # Criando o arquivo tar e adicionando os arquivos
                with tarfile.open(backup_filename, "w:gz") as tar:
                    for directory in directories:
                        tar.add(directory)
                
                print(f"Backup concluído: {backup_filename}")

                # Copiando o arquivo para a pasta de backup
                os.chdir("..")
                shutil.move(os.path.join('/home',userdir, dir_for_backup, backup_filename), os.path.join('/home', userdir, backup_dir_name))
                print(f"Arquivo de backup movido para {backup_dir_name}")
        else:
            print(f"O usuário informado {userdir} não existe.")


if __name__ == "__main__":
    backup_dir("usuario", "backup", "meus_documentos")
