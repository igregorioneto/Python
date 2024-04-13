import numpy as np

class Fila:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.numero_elementos = 0
        self.primeiro = -1
        self.ultimo = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    def cheio(self):
        return self.numero_elementos == self.capacidade
    
    def vazio(self):
        return self.numero_elementos == 0
    
    def enfileirar(self, valor):
        if self.cheio():
            print('A fila esta cheia')
            return -1
        elif self.numero_elementos == 0:
            self.primeiro = self.numero_elementos
            self.ultimo = self.numero_elementos
            self.valores[self.numero_elementos] = valor
            self.numero_elementos += 1            
        else:
            self.ultimo = self.numero_elementos
            self.valores[self.numero_elementos] = valor
            self.numero_elementos += 1

    def desenfileirar(self):
        if self.vazio():
            print('A fila esta vazia')
            return        
        valor = self.valores[self.numero_elementos - 1]
        self.primeiro += 1
        self.numero_elementos -= 1
        return valor
    
    def primeiro_fila(self):
        if self.vazio():
            print('A fila esta vazia')
            return -1
        return self.valores[self.primeiro]
    
    def ultimo_fila(self):
        if self.vazio():
            print('A fila esta vazia')
            return -1
        return self.valores[self.ultimo]
    
fila = Fila(5)
fila.enfileirar(1)
fila.enfileirar(2)
fila.enfileirar(3)
fila.enfileirar(4)
fila.enfileirar(5)
# fila.enfileirar(6)
fila.desenfileirar()
fila.desenfileirar()
fila.desenfileirar()
fila.desenfileirar()
fila.desenfileirar()
fila.enfileirar(1)
fila.enfileirar(2)
fila.enfileirar(3)
fila.enfileirar(4)
fila.enfileirar(5)
print(fila.primeiro_fila())
print(fila.ultimo_fila())
