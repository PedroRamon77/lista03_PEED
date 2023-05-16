from pilha import Pilha

def infixa_para_posfixa(expressao):
    precedencia = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    operadores = Pilha()
    posfixa = []
    numeros = '0123456789'
    for caracter in expressao:
        if caracter in numeros:
            posfixa.append(caracter)
        elif caracter == '(':
            operadores.push(caracter)
        elif caracter == ')':
            while operadores.get_top() != '(':
                posfixa.append(operadores.pop())
            operadores.pop()
        elif caracter in precedencia:
            while not operadores.is_empty()  \
                and operadores.get_top() != '(' \
                and precedencia[caracter] <= precedencia[operadores.get_top()]:
                posfixa.append(operadores.pop())
            operadores.push(caracter)
    while not operadores.is_empty():
        posfixa.append(operadores.pop())
    return ''.join(posfixa)

def calcular(expressao):
    pilha = Pilha()
    for c in expressao:
        if c.isdigit():
            pilha.push(int(c))
        elif c in "+-*/":
            b = pilha.pop()
            a = pilha.pop()
            if c == "+":
                pilha.push(a + b)
            elif c == "-":
                pilha.push(a - b)
            elif c == "*":
                pilha.push(a * b)
            elif c == "/":
                pilha.push(a / b)
    return pilha.pop()


s = input("Digite a expressão: ")

posfixa = infixa_para_posfixa(s)

r = calcular(posfixa)

print("Resultado: ",r)