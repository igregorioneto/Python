import numpy as np
class Pilha:
    def __init__(self, capacidade):
        self.__capacidade = capacidade
        self.__topo = -1
        self.__valores = np.empty(self.__capacidade, dtype=int)

    def __pilha_cheia(self):
        if self.__topo == self.__capacidade - 1:
            return True
        return False
    
    def __pilha_vazia(self):
        if self.__topo == -1:
            return True
        return False
    
    def empilhar(self, valor):
        if self.__pilha_cheia():
            return 'A pilha esta cheia'
        self.__topo += 1
        self.__valores[self.__topo] = valor
    
    def desempilhar(self):
        if self.__pilha_vazia():
            return 'A pilha esta vazia'
        self.__topo -= 1

    def ver_topo(self):
        if self.__topo != -1:
            return self.__valores[self.__topo]
        return -1
    
pilha = Pilha(5)
print(pilha.ver_topo())
pilha.empilhar(1)
pilha.empilhar(2)
pilha.empilhar(3)
pilha.empilhar(4)
print(pilha.empilhar(5))
print(pilha.empilhar(6))
print(pilha.ver_topo())
print(pilha.desempilhar())
print(pilha.ver_topo())