with open('./Entrada_de_Dados/grafo_1_1_5_6.txt','r') as arquivo:
    entrada = arquivo.read()
print(type(entrada))
matriz =[]

for linha in entrada:
    elementos = entrada.slipt(' ')
    numeros = [int(elemento)for elemento in elementos]
    matriz.append(numeros) 
    
