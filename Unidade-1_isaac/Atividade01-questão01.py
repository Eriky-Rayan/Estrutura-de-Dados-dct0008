valor = False

def e_multiplo(n, m):
    n = int(input("Digite um número n: "))
    m = int(input("Digite um número m: "))
    if n % m == 0:
        print(f"{n} é múltiplo de {m}.")
        valor = True
        print(valor)
    else:
        print(f"{n} não é múltiplo de {m}.")
        valor = False
        print(valor)
    return valor

e_multiplo(0, 0)