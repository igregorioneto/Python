'''
Monitorar e Gerenciar tarefas de firewall em um sistema Linux.
Usando Fila (Queue) para enfileirar solicitações de modificação
de regras de firewall.
'''

from fila import Fila

class SolicitacaoFirewall:
    def __init__(self, acao, ip, porta, protocolo):
        self.acao = acao
        self.ip = ip
        self.porta = porta
        self.protocolo = protocolo

class GerenciadorFirewall:
    def __init__(self):
        self.fila_solicitacoes = Fila()

    def adicionar_solicitacao(self, acao, ip, porta, protocolo):
        solicitacao = SolicitacaoFirewall(acao, ip, porta, protocolo)
        self.fila_solicitacoes.enfileirar(solicitacao)

    def processar_solicitacoes(self):
        while not self.fila_solicitacoes.vazia():
            solicitacao = self.fila_solicitacoes.desenfileirar()
            if solicitacao.acao == "bloquear":
                # Aplica regra de bloqueio do Firewall
                 print(f"Regra de bloqueio aplicada para {solicitacao.ip}:{solicitacao.porta}/{solicitacao.protocolo}")
            elif solicitacao.acao == "permitir":
                # Aplica regra de permissão do Firewall
                print(f"Regra de permissão aplicada para {solicitacao.ip}:{solicitacao.porta}/{solicitacao.protocolo}")

# Exemple of use
if __name__ == "__main__":
    gerenciador_firewall = GerenciadorFirewall()
    gerenciador_firewall.adicionar_solicitacao("bloquear", "192.168.1.100", 80, "TCP")
    gerenciador_firewall.adicionar_solicitacao("permitir", "10.0.0.1", 22, "SSH")
    gerenciador_firewall.processar_solicitacoes()
    