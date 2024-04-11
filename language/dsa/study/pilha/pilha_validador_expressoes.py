import numpy as np

class Pilha:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.topo = -1
        self.valores = np.chararray(self.capacidade, unicode= True)

    def __pilha_cheia(self):
        return self.topo == self.capacidade - 1
    
    def pilha_vazia(self):
        return self.topo == -1
    
    def empilhar(self, valor):
        if self.__pilha_cheia():
            print('A pilha esta cheia') 
            return -1
        else:
            self.topo += 1
            self.valores[self.topo] = valor

    def desempilhar(self):
        if self.pilha_vazia():
            print("A pilha esta vazia")
            return -1
        else:
            valor = self.valores[self.topo]
            self.topo -= 1
            return valor
        
    def ver_topo(self):
        if self.topo != -1:
            return self.valores[self.topo]
        else:
            return -1
            
expressao = str(input('Digite a expressão: '))
pilha = Pilha(len(expressao))

for i in range(len(expressao)):
    ch = expressao[i]
    if ch == '{' or ch == '[' or ch == '(':
        pilha.empilhar(ch)
    elif ch == '}' or ch == ']' or ch == ')':
        if not pilha.pilha_vazia():
            chx = str(pilha.desempilhar())
            if (ch == '}' and chx != '{') or (ch == ']' and chx != '[') or (ch == ')' and chx != '('):
                print(f"Erro {ch} na posicao {i}")
                break
        else:
            print(f"Erro {ch} na posicao {i}")
            
if not pilha.pilha_vazia():
    print('Erro!')

    
