'''
Fila(Queues) segue o princípio FIFO(First In, First Out),
que o primeiro elemento a entrar é o primeiro a sair.
'''

class Fila:
    def __init__(self):
        self.items = []

    def vazia(self):
        return self.items == []
    
    def enfileirar(self, item):
        self.items.append(item)

    def desenfileirar(self):
        return self.items.pop(0)
    
    def frente(self):
        return self.items[0]
    
    def tamanho(self):
        return len(self.items)
    
# Example of use
fila = Fila()
fila.enfileirar(1)
fila.enfileirar(2)
fila.enfileirar(3)
print("Elementos da fila:")
while not fila.vazia():
    print(fila.desenfileirar())