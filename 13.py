from pilha import Pilha

def transforma(binario):
    pilha = Pilha()
    
    for p in binario:
        pilha.push(int(p))
   
    potencia = 0
    somaPotencias = 0
     
    while not pilha.is_empty():
        somaPotencias += pilha.pop() * (2 ** potencia)
        potencia += 1
    
    return somaPotencias
    
numero = input("Digite um número binário: ")

decimal = transforma(numero)
print(" número em decimal: ", decimal)