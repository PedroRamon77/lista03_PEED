from pilha import Pilha

def parenteses(expressao):
    pilha = Pilha()
    for caractere in expressao:
        if caractere == '(':
            pilha.push(caractere)
        elif caractere == ')':
            if pilha.is_empty():
                return False
            else:
                pilha.pop()
    return pilha.is_empty()

expressao = input("Digite uma expressão: ")

r = parenteses(expressao)

if r == True:
    print("\nOs parênteses estão balanceados")
else:
    print("\nOs parênteses não estão balanceados")