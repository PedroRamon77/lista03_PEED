from pilha import Pilha

def conversorHexParaDecimal(hexadecimal):
    pilha = Pilha()
    for char in hexadecimal:
        if char.isdigit():
            pilha.push(int(char))
        elif char.isalpha():
            # Converter caracteres A-F para valores numéricos
            valor = ord(char.upper()) - ord('A') + 10
            pilha.push(valor)

    decimal = 0
    posicao_decimal = 0
    while not pilha.is_empty():
        digit = pilha.pop()
        decimal += digit * (16 ** posicao_decimal)
        posicao_decimal += 1

    return decimal

hexadecimal = input("Digite um número hexadecimal: ")

decimal = conversorHexParaDecimal(hexadecimal)

print("Número decimal:", decimal)
