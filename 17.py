from pilha import Pilha

def conversorOctalParaDecimal(octal):
    pilha = Pilha()
    for char in octal:
        if char.isdigit():
            pilha.push(int(char))

    decimal = 0
    posicao_decimal = 0
    while not pilha.is_empty():
        digit = pilha.pop()
        decimal += digit * (8 ** posicao_decimal)
        posicao_decimal += 1

    return decimal

octal = input("Digite um número octal: ")

decimal = conversorOctalParaDecimal(octal)

print("Número decimal:", decimal)