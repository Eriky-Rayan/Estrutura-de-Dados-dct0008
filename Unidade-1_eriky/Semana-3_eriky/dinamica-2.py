'''
verifique os elementos que se repetem e
coloque eles em uma lista.
'''

def num_repetido(lista):
    repete = []
    cont = 0
    for i in lista:
        for j in lista:
            if j == i:
                cont += 1
                if cont >= 2 and j not in repete:
                    repete.append(j)
        cont = 0
    return repete

def num_repetido_2(lista):
    repete = []
    for i in range (0,len(lista)):
        for j in range (0, len(lista)):
            if i != j and lista[i] == lista[j]:
                repete.append(lista[i])
    return repete
                

if __name__ == "__main__":
    numeros = [1,1,2,2,4,5,5]
    resp = num_repetido(numeros)
    print(resp)