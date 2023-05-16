from pilha import Pilha

def palindromo(numero):
    pilha = Pilha()
    for digito in numero:
        pilha.push(digito)

    palindromo = True
    for digito in numero:
        if digito != str(pilha.pop()):
            palindromo = False
            break

    return palindromo

numero = input("Digite um número: ")

r = palindromo(numero)

if r == True:
    print("\nO número",numero,"é um palíndromo")
else:
    print("\nO número",numero,"não é um palíndromo")
