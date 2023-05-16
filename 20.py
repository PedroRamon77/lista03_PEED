from pilha import Pilha

def conversorBinParaHex(numero_binario):
    pilha = Pilha()
    
    decimal = 0
    for digito in numeroBin:
        if digito != '0' and digito != '1':
            raise Exception("Número binário inválido")
        decimal = decimal * 2 + int(digito)
    
    while decimal > 0:
        resto = decimal % 16
        pilha.push(resto)
        decimal //= 16
    
    if pilha.is_empty():
        return '0'
    
    numeroHex = ''
    while not pilha.is_empty():
        valor = pilha.pop()
        if valor < 10:
            numeroHex += str(valor)
        else:
            numeroHex += chr(ord('A') + valor - 10)
    
    return numeroHex

numeroBin = input("Digite um número binário: ")

numeroHex = conversorBinParaHex(numeroBin)

print("Número hexadecimal:", numeroHex)
