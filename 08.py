from pilha import Pilha

def conversorDecParaHexa(num):
    pilha = Pilha()
    while num > 0:
        resto = num % 16
        if resto < 10:
            pilha.push(resto)
        else:
            pilha.push(chr(resto + 55))
        num //= 16

    hexadecimal = ''
    while not pilha.is_empty():
        hexadecimal += str(pilha.pop())

    return hexadecimal

numDec = int(input("Digite um número decimal: "))

hexadecimal = conversorDecParaHexa(numDec)

print("Convertido para hexadecimal é:",hexadecimal)