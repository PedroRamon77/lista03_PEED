from pilha import Pilha

def is_operador(caractere):
    return caractere in "+-*/"

def precedencia(operador):
    if operador in "+-":
        return 1
    elif operador in "*/":
        return 2
    return 0

def converter_para_rpn(expressao):
    pilha = Pilha()
    rpn = ""
    for caractere in expressao:
        if caractere.isdigit():
            rpn += caractere
        elif is_operador(caractere):
            while not pilha.is_empty() and is_operador(pilha.get_top()) and precedencia(pilha.get_top()) >= precedencia(caractere):
                rpn += pilha.pop()
            pilha.push(caractere)
        elif caractere == "(":
            pilha.push(caractere)
        elif caractere == ")":
            while not pilha.is_empty() and pilha.get_top() != "(":
                rpn += pilha.pop()
            if not pilha.is_empty() and pilha.get_top() == "(":
                pilha.pop()

    while not pilha.is_empty():
        rpn += pilha.pop()

    return rpn

expressao = input("Digite a expressão matemática: ")

expressao_rpn = converter_para_rpn(expressao)

print("\nExpressão em notação polonesa reversa (RPN):", expressao_rpn)
