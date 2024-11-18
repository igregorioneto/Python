class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class BinaryTree:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = Node(valor)
        else:
            self._inserir(self.raiz, valor)

    def _inserir(self, atual, valor):
        if valor < atual.valor:
            if atual.esquerda is None:
                atual.esquerda = Node(valor)
            else:
                self._inserir(atual.esquerda, valor)
        else:
            if atual.direita is None:
                atual.direita = Node(valor)
            else:
                self._inserir(atual.direita, valor)

    def exibir_em_ordem(self):
        self._exibir_em_ordem(self.raiz)

    def _exibir_em_ordem(self, atual):
        if atual is not None:
            self._exibir_em_ordem(atual.esquerda)
            print(atual.valor, end=" ")
            self._exibir_em_ordem(atual.direita)

    def contar_folhas(self):
       return self._contar_folhas(self.raiz)
    
    def _contar_folhas(self, atual):
        if atual is None:
            return 0
        if atual.esquerda is None and atual.direita is None:
            return 1
        return self._contar_folhas(atual.esquerda) + self._contar_folhas(atual.direita)
            
if __name__ == "__main__":
    arvore = BinaryTree()

    arvore.inserir(10)
    arvore.inserir(5)
    arvore.inserir(15)
    arvore.inserir(3)
    arvore.inserir(7)
    arvore.inserir(13)
    arvore.inserir(18)

    print("Valores da árvore em ordem:")
    arvore.exibir_em_ordem()
    count = arvore.contar_folhas()
    print("Quantidade de Folhas: ", count)