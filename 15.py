from pilha import Pilha

def converterListaParaBinario(lista):
    pilha = Pilha()
    for num_str in lista:
        num = int(num_str)
        binario = ""
        if num == 0:
            binario = "0"
        else:
            while num > 0:
                bit = num % 2
                pilha.push(str(bit))
                num //= 2
            while not pilha.is_empty():
                binario += pilha.pop()
        pilha.push(binario)

    numero_binario = ""
    while not pilha.is_empty():
        numero_binario += pilha.pop()

    return numero_binario

listaNum = input("Digite uma sequência de números separados por espaço: ").split()

numeroBinario = converterListaParaBinario(listaNum)

print("Número binário:", numeroBinario)
