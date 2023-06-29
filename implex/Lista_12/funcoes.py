def  achaMaximo(vetor):
    maximo  = 0
    for i in vetor:
        if(i >maximo):
            maximo =i
    return maximo
def indexMax(vetor):
    i=0
    i=int(i)
    achou=False
    while(i<len(vetor)and not achou): 
        if(vetor[i] == achaMaximo(vetor)):
           achou = True
           return i      
        else:
            i=i+1
