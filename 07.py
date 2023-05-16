from pilha import Pilha

def conversorDecParaOctal(num):
    pilha = Pilha()
    while num > 0:
        resto = num % 8
        pilha.push(resto)
        num //= 8

    octal = ''
    while not pilha.is_empty():
        octal += str(pilha.pop())

    return octal

numDec = int(input("Digite um número decimal: "))

octal = conversorDecParaOctal(numDec)

print("\nConvertido para octal é:",octal)