import numpy as np

class Pilha:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.topo = -1
        self.valores = np.chararray(self.capacidade, unicode= True)

    def vazio(self):
        return self.topo == -1
    
    def __cheio(self):
        return self.topo == self.capacidade - 1
    
    def empilhar(self, valor):
        if self.__cheio():
            print('A pilha esta cheia')
            return -1
        else:
            self.topo += 1
            self.valores[self.topo] = valor

    def desempilhar(self):
        if self.vazio():
            print('A pilha esta vazia')
            return -1
        else:
            valor = self.valores[self.topo]
            self.topo -= 1
            return valor    

    def valor_topo(self):
        if self.vazio():
            print('A pilha esta vazia')
            return -1
        return self.valores[self.topo]
    
    def validador(self, expressao):
        for i in range(len(expressao)):
            ch = expressao[i]    
            if ch == '(':
                self.empilhar(ch)
            elif ch == ')':
                if self.vazio() or self.desempilhar() != '(':
                    print(f'Erro: Parêntese desbalanceado na posição {i}')
                    return False
            
        if not self.vazio():            
            print(f'Erro: Parêntese desbalanceado no final da expressão')
            return False
        
        return True

expressao = str(input('Digite a expressão: '))
pilha = Pilha(len(expressao))
print(pilha.validador(expressao))