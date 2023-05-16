from pilha import Pilha

def ordenarLista(lista):
    pilha = Pilha()
    for num in lista:
        while not pilha.is_empty() and pilha.get_top() < num:
            lista.append(pilha.pop())
        pilha.push(num)
    listaOrdenada = []
    while not pilha.is_empty():
        listaOrdenada.append(pilha.pop())
    return listaOrdenada

lista = []
tam = int(input("Digite o tamanho da lista: "))

for i in range(tam):
    num = int(input("Digite os números da lista: "))
    lista.append(num)
    

listaOrdenada = ordenarLista(lista)
print("\nOrdem Crescente: \n", listaOrdenada)
