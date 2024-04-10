import numpy as np

class VetorOrdenado:
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
                print(f"{i} - {self.valores[i]}")

    def insere(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade máxima atingida.')
            return
        
        posicao = 0
        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.valores[i] > valor:
                break
            if i == self.ultima_posicao:
                posicao = i + 1
        
        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x + 1] = self.valores[x]
            x -= 1

        self.valores[posicao] = valor
        self.ultima_posicao += 1

    def pesquisar(self, valor):
        for i in range(self.ultima_posicao + 1):
            if valor == self.valores[i]:
                return i
        return -1
    
    # O(n)
    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]
            self.ultima_posicao -= 1

    # Pesquisa Linear X Pesquisa Binária
    def pesquisa_linear(self, valor):
        for i in range(self.ultima_posicao + 1):
            if self.valores[i] > valor:
                return -1
            if self.valores[i] == valor:
                return i
            
    def pesquisa_binaria(self, valor):
        limite_inferior = 0
        limite_superior = self.ultima_posicao

        while True:
            posicao_atual = int((limite_inferior + limite_superior) / 2)
            if self.valores[posicao_atual] == valor:
                return posicao_atual
            elif limite_inferior > limite_superior:
                return -1
            else:
                if self.valores[posicao_atual] < valor:
                    limite_inferior = posicao_atual + 1
                else:
                    limite_superior = posicao_atual - 1

    def fundir(self, vetor):
        i = j = k = 0

        while i < self.ultima_posicao + 1 and j < vetor.ultima_posicao + 1:
            if self.valores[i] < vetor.valores[j]:
                self.valores[k] = self.valores[i]
                i += 1
            else:
                self.valores[k] = vetor.valores[j]
                j += 1
            k += 1

        while i < self.ultima_posicao + 1:
            self.valores[k] = self.valores[i]
            i += 1
            k += 1

        while j < vetor.ultima_posicao + 1:
            self.valores[k] = vetor.valores[j]
            j += 1
            k += 1

        self.ultima_posicao = k - 1


vetor = VetorOrdenado(10)
vetor.imprime()
vetor.insere(8)
vetor.insere(2)
vetor.insere(3)
vetor.insere(4)
vetor.imprime()
print('-------')
print(vetor.pesquisa_binaria(8))

vetor2 = VetorOrdenado(10)
vetor2.insere(8)
vetor2.insere(2)
vetor2.insere(3)
vetor2.insere(4)

vetor.fundir(vetor2)

vetor.imprime()
    