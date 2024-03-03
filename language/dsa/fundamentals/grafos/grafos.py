class Grafo:
    def __init__(self):
        self.vertices = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = []

    def adicionar_aresta(self, origem, destino):
        if origem in self.vertices and destino in self.vertices:
            self.vertices[origem].append(destino)
            self.vertices[destino].append(origem)

    def __str__(self):
        result = ""
        for vertice in self.vertices:
            result += f"{vertice}: {', '.join(self.vertices[vertice])}\n"
        return result
    
# Exemple of use:
if __name__ == "__main__":
    grafo = Grafo()
    grafo.adicionar_vertice('A')
    grafo.adicionar_vertice('B')
    grafo.adicionar_vertice('C')
    grafo.adicionar_vertice('D')
    grafo.adicionar_vertice('E')
    grafo.adicionar_vertice('F')

    grafo.adicionar_aresta('A', 'B')
    grafo.adicionar_aresta('A', 'C')
    grafo.adicionar_aresta('B', 'D')
    grafo.adicionar_aresta('C', 'E')
    grafo.adicionar_aresta('D', 'F')
    grafo.adicionar_aresta('E', 'F')

    print(grafo)
