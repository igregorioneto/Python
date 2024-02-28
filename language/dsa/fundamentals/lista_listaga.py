# Criando a classe Nó
class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

# Criando a classe da Lista ligada
class ListaLigada:
    def __init__(self):
        self.cabeca = None
    
    def inserir(self, valor):
        novo_no = No(valor)
        if self.cabeca == None:
            self.cabeca = novo_no
        else:
            atual = self.cabeca
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_no

    def imprimir(self):
        atual = self.cabeca
        while atual:
            print(atual.valor, end= " -> ")
            atual = atual.proximo
        print("None")

    def buscar_valor(self, valor):
        atual = self.cabeca
        while atual:
            if atual.valor == valor:
                print(f"O valor {valor} foi encontrado")
                return
            atual = atual.proximo
        print(f"O valor {valor} não existe na lista")


# Exemplo de uso:
lista = ListaLigada()
lista.inserir(1)
lista.inserir(2)
lista.inserir(3)
lista.inserir(4)
lista.inserir(5)
lista.imprimir()
lista.buscar_valor(6)
