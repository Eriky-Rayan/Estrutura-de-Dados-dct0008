lista = [1,1,1,1,1,1,1,1,1,1,1,1,1,1]
n = int(input("Digite o número a ser buscado: "))


def função(lista, n):
    contador = 0 
    for i in lista:
        if i == n:
            contador += 1
    return contador

print(f"O número {n} aparece {função(lista, n)} vezes na lista.")