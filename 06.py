from pilha import Pilha

def caracteres(s):
    pilha = Pilha()
    for c in s:
        if c in '([{':
            pilha.push(c)
        elif c in ')]}':
            if pilha.is_empty():
                return False
            topo = pilha.pop()
            if (c == ')' and topo != '(') or (c == ']' and topo != '[') or (c == '}' and topo != '{'):
                return False

    return pilha.is_empty()

s = input("Digite uma string: ")

r = caracteres(s)

if r== True:
    print("Os caracteres estão balanceados")
else:
    print("Os caracteres não estão balanceados")