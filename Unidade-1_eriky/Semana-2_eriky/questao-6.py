'''
Questão 06. A partir de uma lista de nomes ['ana', 'bia', 'caio'], crie um dicionário onde a chave é o nome
e o valor é o número de letras desse nome.
'''

nomes = ['ana', 'bia', 'caio']
dicio = {}

for nomes in nomes:
    dicio[nomes] = len(nomes)
print(dicio)