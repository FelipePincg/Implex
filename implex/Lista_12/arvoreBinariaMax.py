import funcoes
class arvoreBinariaMax:
        def __init__(self,value):
            self.value = value
            self.esq   = None
            self.dir   = None
 
def arvoreMax(vetor):
        if not vetor:
            return None 
        max_valor = funcoes.achaMaximo(vetor)
        max_index = funcoes.indexMax(vetor)

        raiz = arvoreBinariaMax(max_valor)
        raiz.esq = arvoreMax(vetor[:max_index])
        raiz.dir = arvoreMax(vetor[max_index+1:])

        return raiz

# def percurso_inorder(raiz):
#      if raiz:
#         percurso_inorder(raiz.esq)
#         print(raiz.value,end=' ')
#         percurso_inorder(raiz.dir)

# def  percurso_posordem(raiz):
#     if raiz :
#         percurso_posordem(raiz.esq)
#         percurso_posordem(raiz.dir)
#         print(raiz.value, end=' ')

# def percurso_preordem(raiz):
#     if raiz:
#          print(raiz.value,end=' ')
#          percurso_preordem(raiz.esq)
#          percurso_preordem(raiz.dir)

def percurso_inorder(raiz,saida):
     if raiz:
        percurso_inorder(raiz.esq,saida)
        saida.write(str(raiz.value) + " ")
        percurso_inorder(raiz.dir,saida)

def  percurso_posordem(raiz,saida):
    if raiz :
        percurso_posordem(raiz.esq,saida)
        percurso_posordem(raiz.dir,saida)
        saida.write(str(raiz.value) + " ")

def percurso_preordem(raiz,saida):
    if raiz:
        saida.write(str(raiz.value)+" ")
        percurso_preordem(raiz.esq,saida)
        percurso_preordem(raiz.dir,saida)

def  processa_sequencia(entrada,saida):
     with open(entrada,'r') as arquivo_entrada:
          num_sequences = int(arquivo_entrada.readline())
          with open(saida,'w')as arquivo_saida:
               
               vetor  =  arquivo_entrada.readline()
               print(vetor)
               for _ in range(num_sequences):
                    arquivo_entrada.readline()
                    linha_dados = arquivo_entrada.readline().split() 
                    qtd_dados = len(linha_dados)
                    dados = list(map(int,linha_dados))


                    arvore = arvoreMax(dados)
                    
                    arquivo_saida.write("Inorder: ")
                    percurso_inorder(arvore,arquivo_saida)
                    arquivo_saida.write("\n")

                    arquivo_saida.write("Preorder: ")
                    percurso_preordem(arvore,arquivo_saida)
                    arquivo_saida.write("\n")

                    arquivo_saida.write("Posorder: ")
                    percurso_posordem(arvore,arquivo_saida)
                    arquivo_saida.write("\n")

            



    
