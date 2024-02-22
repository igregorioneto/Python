from flask import Flask, request, jsonify
import sys
import os
from fabric import Connection
import tarfile
import shutil
from datetime import datetime

app = Flask(__name__)

def backup_dir(userdir, backup_dir_name, dir_for_backup):
    # Verifica sistema linux
    if sys.platform.startswith('linux'):
        backup_info = []
        #Vai para o diretório Home
        backup_info.append("Iniciando o backup...")
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
                backup_info.append(f"Diretório {dir_for_backup} para backup não existe...")
            else:
                # Verifica se a pasta de backup existe, caso não exista é criada
                if backup_dir_name in directories:
                    backup_info.append(f"Diretório {backup_dir_name} existe...")
                else:
                    os.mkdir(backup_dir_name)
                    backup_info.append(f"Criando pasta de {backup_dir_name}")
                
                # Listando diretorios novamente
                directories = os.listdir("./")
                backup_info.append(directories)

                # Entra na pasta para realizar backup dos arquivos
                os.chdir(dir_for_backup)    
                directories = os.listdir("./")
                backup_info.append(f"Arquivos para backup: {directories}")

                # Cria o nome do arquivo para backup com a data atual
                date_today = datetime.now().strftime("%Y-%m-%d")
                backup_filename = f"backup_{date_today}.tar.gz"

                # Criando o arquivo tar e adicionando os arquivos
                with tarfile.open(backup_filename, "w:gz") as tar:
                    for directory in directories:
                        tar.add(directory)
                
                backup_info.append(f"Backup concluído: {backup_filename}")

                # Copiando o arquivo para a pasta de backup
                os.chdir("..")
                shutil.move(os.path.join('/home',userdir, dir_for_backup, backup_filename), os.path.join('/home', userdir, backup_dir_name))
                backup_info.append(f"Arquivo de backup movido para {backup_dir_name}")
        else:
            backup_info.append(f"O usuário informado {userdir} não existe.")

    return backup_info

@app.route("/backup", methods=['POST'])
def backup():
    data = request.get_json()
    userdir = data.get('userdir')
    backup_dir_name = data.get('backup_dir_name')
    dir_for_backup = data.get('dir_for_backup')

    backup_result = backup_dir(userdir=userdir, backup_dir_name=backup_dir_name, dir_for_backup=dir_for_backup)
    return jsonify({ "backup_result":backup_result })

if __name__ == "__main__":
    app.run(debug=True)
