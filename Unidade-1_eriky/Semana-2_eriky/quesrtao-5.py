'''
Questão 05. Crie uma estrutura que represente uma lista de alunos, onde cada aluno é um dicionário
contendo "nome" e uma lista de "notas". Como você acessaria a segunda nota do primeiro aluno?
'''

alunos = [
    {"nome": "João", "notas": [7.5, 8.0, 6.5]},
    {"nome": "Maria", "notas": [9.0, 8.5, 7.0]}
]
segunda_nota = alunos[0]["notas"][1]
print(segunda_nota)