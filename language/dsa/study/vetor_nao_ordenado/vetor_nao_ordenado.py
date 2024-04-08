import numpy as np

class VetorNaoOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    # O(n)
    def imprime(self):
        if self.ultima_posicao == -1:
            print('O vetor esta vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, ' - ', self.valores[i])

    def inserir(self, valor):  
        self.redimensionar()             
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade máxima atingida')            
        else:
            self.ultima_posicao += 1
            self.valores[self.ultima_posicao] = valor

    def pesquisar(self, valor):
        for i in range(self.ultima_posicao + 1):
            if valor == self.valores[i]:
                return i
        return -1
    
    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]
            
            self.ultima_posicao -= 1

    def redimensionar(self):
        if self.ultima_posicao == self.capacidade - 1:
           nova_capacidade = self.capacidade * 2
           novo_vetor = np.empty(nova_capacidade, dtype=int)

           for i in range(self.capacidade):
               novo_vetor[i] = self.valores[i]

           self.valores = novo_vetor
           self.capacidade = nova_capacidade


vetor = VetorNaoOrdenado(5)
vetor.imprime()
print('-----')
vetor.inserir(1)
vetor.inserir(2)
vetor.inserir(3)
vetor.inserir(4)
vetor.inserir(5)
vetor.inserir(5)
vetor.imprime()
print('-----')

print(vetor.pesquisar(3))
print('-----')
print(vetor.pesquisar(5))
print('-----')

vetor.excluir(3)
vetor.imprime()
print('-----')

vetor.excluir(5)
vetor.imprime()
print('-----')

vetor.excluir(1)
vetor.imprime()
print('-----')
vetor.inserir(1)
vetor.inserir(2)
vetor.inserir(3)
vetor.inserir(4)
vetor.inserir(5)
vetor.inserir(5)
vetor.inserir(1)
vetor.inserir(2)
vetor.inserir(3)
vetor.inserir(4)
vetor.inserir(5)
vetor.inserir(5)
vetor.imprime()


