def Quicksort(vetor,inicio,fim):
    if(inicio<fim):
        meio = Particiona(vetor,inicio,fim)
        Quicksort(vetor,inicio,meio-1)  
        Quicksort(vetor,meio+1,fim)  
        
def  Particiona(vetor,inicio,fim):
    base =vetor[inicio]
    i = inicio
    f = fim
    while(i<f):
        while(vetor[f]>= base and i<f):
            f=f-1
        if(i<f):
            vetor[i]=vetor[f]
            vetor         