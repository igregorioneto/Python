'''
Estrutura de dados hierárquica que consistem
em nós conectados por arestas.
'''
class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    # Inserir
    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir_recursivo(self.raiz, valor)
        
    # Inserir de forma recursiva
    def _inserir_recursivo(self, no, valor):
        if valor < no.valor:
            if no.esquerda is None:
                no.esquerda = No(valor)
            else:
                self._inserir_recursivo(no.esquerda, valor)
        elif valor > no.valor:
            if no.direita is None:
                no.direita = No(valor)
            else:
                self._inserir_recursivo(no.direita, valor)

    # Em ordem
    def em_ordem(self):
        self._em_ordem_recursivo(self.raiz)

    # Em ordem de forma recursiva
    def _em_ordem_recursivo(self, no):
        if no is not None:
            self._em_ordem_recursivo(no.esquerda)
            print(no.valor)
            self._em_ordem_recursivo(no.direita)

# Example of use:
if __name__ == "__main__":
    arvore = ArvoreBinariaBusca()
    arvore.inserir(5)
    arvore.inserir(3)
    arvore.inserir(7)
    arvore.inserir(4)
    arvore.inserir(1)
    arvore.em_ordem()
    