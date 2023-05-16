from pilha import Pilha

def inverter_palavras(frase):
    palavras = frase.split()
    pilha = Pilha()
    for palavra in palavras:
        pilha.push(palavra)
    nova_frase = ""
    while not pilha.is_empty():
        nova_frase += pilha.pop() + " "
    return nova_frase.strip()

frase = input("Digite uma frase: ")
frase_invertida = inverter_palavras(frase)
print("Frase invertida: ", frase_invertida)