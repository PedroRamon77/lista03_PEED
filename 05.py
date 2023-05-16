from pilha import Pilha

def palindromo(s):
    pilha = Pilha()
    for c in s:
        pilha.push(c)

    for c in s:
        if c != pilha.pop():
            return False

    return True

s = input("Digite uma string: ")

r = palindromo(s)

if r == True:
    print(s,"é um palíndromo")
else:
    print(s,"não é um palíndromo")