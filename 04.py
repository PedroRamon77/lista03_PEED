from pilha import Pilha

def converter_dec_bin(n):
    p = Pilha()
    q = n
    while n > 0:
        r = n % 2
        n = n // 2
        p.push(r)
       
    return p
       
n = int(input("Número Decimal: "))

r = converter_dec_bin(n)
print("\n")

while not r.is_empty():
    print(r.pop())
    
