from pilha import Pilha

def converterParaDecimal(string):
    pilha = Pilha()
    for char in string:
        if char.isdigit():
            pilha.push(int(char))

    decimal = 0
    posicao_decimal = 0
    while not pilha.is_empty():
        digit = pilha.pop()
        decimal += digit * (10 ** posicao_decimal)
        posicao_decimal += 1

    return decimal

string_numeros = input("Digite uma sequência de números: ")

numero_decimal = converterParaDecimal(string_numeros)

print("Número decimal:", numero_decimal)