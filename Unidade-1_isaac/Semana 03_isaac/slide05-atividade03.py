lista = [2,2,2,3,4,4,5,6,7,8]
lista_repetidos = []

def funcao(lista):
    for i in lista:
        if lista.count(i) > 1:
            if i not in lista_repetidos:
                lista_repetidos.append(i)
            else:
                lista_repetidos.append(i)
    return lista_repetidos

print(funcao(lista))