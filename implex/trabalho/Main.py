import math

def calcular_distancia_euclidiana(x1, y1, x2, y2):
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distancia

def calcular_distancias_tsp(arquivo):
    vertices = []
    with open(arquivo, 'r') as file:
        for line in file:
            if line.startswith("EOF"):
                break
            parts = line.strip().split()
            identificador = int(parts[0])
            x = float(parts[1])
            y = float(parts[2])
            vertices.append((identificador, x, y))

    num_vertices = len(vertices)
    distancias = [[0] * num_vertices for _ in range(num_vertices)]

    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            identificador1, x1, y1 = vertices[i]
            identificador2, x2, y2 = vertices[j]
            distancia = calcular_distancia_euclidiana(x1, y1, x2, y2)
            distancias[i][j] = distancia
            distancias[j][i] = distancia

    return distancias

# Exemplo de uso
arquivo_tsp = 'att48.tsp.txt'
distancias = calcular_distancias_tsp(arquivo_tsp)
print(distancias)

