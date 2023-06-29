class Grafo:
    def __init__(self):
        self.grafo = {}
        
    def adicionar_vertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = []
            
    def adicionar_aresta(self, vertice1, vertice2):
        if vertice1 in self.grafo and vertice2 in self.grafo:
            self.grafo[vertice1].append(vertice2)
            self.grafo[vertice2].append(vertice1)
            
    def remover_aresta(self, vertice1, vertice2):
        if vertice1 in self.grafo and vertice2 in self.grafo:
            self.grafo[vertice1].remove(vertice2)
            self.grafo[vertice2].remove(vertice1)
            
    def verificar_aresta(self, vertice1, vertice2):
        if vertice1 in self.grafo and vertice2 in self.grafo:
            return vertice2 in self.grafo[vertice1]
        return False
    
    def obter_vizinhos(self, vertice):
        if vertice in self.grafo:
            return self.grafo[vertice]
        return []
    
    def imprimir_grafo(self):
        for vertice in self.grafo:
            print(vertice, "->", self.grafo[vertice])
