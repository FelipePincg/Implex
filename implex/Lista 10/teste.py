# Função para adicionar uma aresta à lista de arestas
def adicionar_aresta(lista_arestas, origem, destino):
    aresta = {'origem': origem, 'destino': destino}
    lista_arestas.append(aresta)

# Exemplo de uso
lista_arestas = []

# Adicionando arestas
adicionar_aresta(lista_arestas, 1, 2)
adicionar_aresta(lista_arestas, 2, 3)
adicionar_aresta(lista_arestas, 3, 4)

# Imprimindo a lista de arestas
for aresta in lista_arestas:
    print(f"Aresta: {aresta['origem']} -> {aresta['destino']}")
