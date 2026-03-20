'''
função recebe lista e elemento para busca,
verifique quantas vezes o elemento aparece na lista.
'''
#função 1

def conta_item_lista(lista, item):
    cont = 0
    for i in lista:
        if i == item:
            cont+= 1
    print(cont)

def conta_item_lista_2(lista, item):
    cont = lista.count(item)
    print(cont)

if __name__ == "__main__":
    numeros = [0,1,1,2,3,4,5]
    conta_item_lista(numeros, 1)