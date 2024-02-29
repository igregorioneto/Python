import time, os

'''
Monitorar e Registrar o acesso a arquivos críticos no sistema Linux.
'''
class RegistroAcesso:
    def __init__(self, caminho, tipo_acesso):
        self.caminho = caminho
        self.tipo_acesso = tipo_acesso
        self.horario_acesso = time.strftime('%Y-%m-%d %H:%M:%S')

class PilhaAcessos:
    def __init__(self):
        self.acessos = []

    def empilhar_acesso(self, caminho, tipo_acesso):
        acesso = RegistroAcesso(caminho, tipo_acesso)
        self.acessos.append(acesso)

    def registrar_acessos(self):
        with open("log_acessos.txt", "a") as arquivo:
            for acesso in self.acessos:
                arquivo.write(f"Caminho: {acesso.caminho}, Tipo de Acesso: {acesso.tipo_acesso}, Horário: {acesso.horario_acesso}\n")

if __name__ == "__main__":
    pilha_acessos = PilhaAcessos()
    pilha_acessos.empilhar_acesso("/etc/passwd", "Leitura")
    pilha_acessos.empilhar_acesso("/var/log/syslog", "Leitura")
    pilha_acessos.registrar_acessos()