'''
Pilha (Stack) segue o princípio LIFO (Last In, First Out),
o que significa que o último elemento inserido é o primeiro a ser removido.
'''
class Stack:
    def __init__(self):
        self.items = []

    def vazia(self):
        return self.items == []
    
    def empilhar(self, item):
        self.items.append(item)

    def desempilhar(self):
        return self.items.pop()

    def topo(self):
        return self.items[-1]
    
    def tamanho(self):
        return len(self.items)
    
# Example of use
pilha = Stack()
pilha.empilhar(1)
pilha.empilhar(2)
pilha.empilhar(3)
print("Elements stack")
while not pilha.vazia():
    print(pilha.desempilhar())