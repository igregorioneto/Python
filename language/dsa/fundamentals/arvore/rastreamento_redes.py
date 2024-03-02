'''
Sistema para rastrear informações da rede em um servidor Linux
e identificar padrões suspeitos.
Usando a Estrutura de Dados Árvore Binária para armazenar
os endereços de IP dos clientes que acessam o servidor e contar
o número de acessos de cada cliente.

Pode ajudar na detecção de atividades suspeitas,
como ataques de negação de serviço (DoS) ou
tentativas de intrusão.
'''

import pcapy
from scapy.all import IP

class No:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contado = 1
        self.esquerda = None
        self.direita = None

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, endereco):
        if self.raiz is None:
            self.raiz = No(endereco)
        else:
            self._inserir_recursivo(self.raiz, endereco)

    def _inserir_recursivo(self, no, endereco):
        if endereco == no.endereco:
            no.contador += 1
        elif endereco < no.endereco:
            if no.esquerda is None:
                no.esquerda = No(endereco)
            else:
                self._inserir_recursivo(no.esquerda, endereco)
        else:
            if no.direita is None:
                no.direita = No(endereco)
            else:
                self._inserir_recursivo(no.direita, endereco)

    def percorrer_em_ordem(self):
        self._percorrer_em_ordem_recursivo(self.raiz)

    def _percorrer_em_ordem_recursivo(self, no):
        if no is not None:
            self._percorrer_em_ordem_recursivo(no.esquerda)
            print(f"Endereço IP: {no.endereco}, Contador: {no.contador}")
            self._percorrer_em_ordem_recursivo(no.direita)

# Função para capturar e analisar pacotes de rede
def capturar_informacoes(interface):
    captura = pcapy.open_live(interface, 65536, True, 100)
    arvore_ips = ArvoreBinariaBusca()

    while True:
        _, pacote = captura.next()
        ip = IP(pacote)
        # Captura pacotes com endereço de IP de origem
        if ip.src:
            arvore_ips.inserir(ip.src)
            arvore_ips.percorrer_em_ordem()

if __name__ == "__main__":
    # Interface de rede para capturar pacotes
    interface = "enp3s0"
    capturar_informacoes(interface)