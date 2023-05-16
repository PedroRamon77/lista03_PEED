from pilha import Pilha

def conevrsorBinParaOctal(numero_binario):
    pilha = Pilha()
    
    decimal = 0
    for digito in numeroBin:
        if digito != '0' and digito != '1':
            raise Exception("Número binário inválido")
        decimal = decimal * 2 + int(digito)
    
    while decimal > 0:
        resto = decimal % 8
        pilha.push(resto)
        decimal //= 8
    
    if pilha.is_empty():
        return '0'
    
    numeroOctal = ''
    while not pilha.is_empty():
        numeroOctal += str(pilha.pop())
    
    return numeroOctal


numeroBin = input("Digite um número binário: ")
numeroOctal = conevrsorBinParaOctal(numeroBin)
print("Número octal: ",numeroOctal)
