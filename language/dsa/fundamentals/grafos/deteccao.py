'''
Sistema de detecção de intrusões para encontrar o menor caminho
entre um computador comprometido e um computador
crítico na rede.
'''

import heapq

class Grafo:
    def __init__(self):
        self.vertices = {}

    def adicionar_vertices(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = {}

    def adicionar_aresta(self, origem, destino, peso):
        if origem in self.vertices and destino in self.vertices:
            self.vertices[origem][destino] = peso

    def dijkstra(self, origem, destino):
        # Inicializa todas as distancias como infinito, medos a origem
        distancia = {v: float('inf') for v in self.vertices}
        distancia[origem] = 0

        # Inicializa a fila de propriedade com a origem
        fila = [(0, origem)]

        while fila:
            # Remove e retorna o vértice com a menor distância da fila de propriedade
            dist_v, v = heapq.heappop(fila)

            # Se o vértice removido é um destino, retorna a distância mínima até ele
            if v == destino:
                return distancia[v]
            
            # Se a distância atual é maior que a distância armazenada, ignora
            if dist_v > distancia[v]:
                continue

            # Para cada vizinho 'u' do vértice 'v'
            for u, peso in self.vertices[v].items():
                # Calcula a nova distância
                nova_dist = dist_v + peso
                # Se a nova distância for menor do que a distância atual
                if nova_dist < distancia[u]:
                    # Atualiza a distância e insere na fila de propriedade
                    distancia[u] = nova_dist
                    heapq.heappush(fila, (nova_dist, u))
        
        # Se o destino não for alcançado, retorna infinito
        return float('inf')

# Exemple of use    
if __name__ == "__main__":
    grafo = Grafo()
    grafo.adicionar_vertices('A')
    grafo.adicionar_vertices('B')
    grafo.adicionar_vertices('C')
    grafo.adicionar_vertices('D')
    grafo.adicionar_vertices('E')
    grafo.adicionar_vertices('F')

    grafo.adicionar_aresta('A', 'B', 1)
    grafo.adicionar_aresta('A', 'C', 2)
    grafo.adicionar_aresta('B', 'D', 3)
    grafo.adicionar_aresta('C', 'E', 4)
    grafo.adicionar_aresta('D', 'F', 5)
    grafo.adicionar_aresta('E', 'F', 6)

    origem = 'A'
    destino = 'F'
    menor_caminho = grafo.dijkstra(origem, destino)
    print(f"O menor caminho entre {origem} e {destino} é de {menor_caminho}")