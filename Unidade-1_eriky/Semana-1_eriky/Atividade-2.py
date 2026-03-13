'''
leitura e validação de dados do usuario (nome, data de nascimento e email).
Autor: Eriky R. B. de Medeiro auxiliado por Copilot
'''

def valida_data(data):
    if len(data) != 10:
        return False
    if data[2] != "/" or data[5] != "/":
        return False
    
    dia_str = data[0:2]
    mes_str = data[3:5]
    ano_str = data[6:10]

    if not (dia_str.isdigit() and mes_str.isdigit() and ano_str.isdigit()):
        return False

    dia = int(dia_str)
    mes = int(mes_str)
    ano = int(ano_str)

    if ano < 1900 or ano > 2100 or mes < 1 or mes > 12:
        return False

    if mes == 2:
        bissexto = (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0))
        if bissexto:
            max_dias = 29
        else:
            max_dias = 28
    elif mes in (4, 6, 9, 11):
        max_dias = 30
    else:
        max_dias = 31

    if dia >= 1 and dia <= max_dias:
        return True
    else:
        return False

def valida_email(email):
    for i in range(len(email)):
        if email[i] == "@":
            for j in range(i+1, len(email)):
                if email[j] == ".":
                    return True
    return False

def ler_nome():
    while True:
        nome = str(input("Digite o nome do usuario: "))
        if len(nome) > 0:
            return nome
        else:
            print("Nome não pode ser vazio. Tente novamente.")

def ler_data_nasc():
    while True:
        data_nasc = str(input("Digite a data de nascimento (dd/mm/aaaa): "))
        if valida_data(data_nasc):
            return data_nasc
        else:
            print("Data de nascimento inválida. Tente novamente.")

def ler_email():
    while True:
        email = str(input("Digite o email do usuario: "))
        if valida_email(email):
            return email
        else:
            print("Email inválido. Tente novamente.")

def cad_usuario():
    nome = ler_nome()
    data_nasc = ler_data_nasc()
    email = ler_email()
    return nome, data_nasc, email

def exib_dados(nome, data_nasc, email):
    print("\n=============== Dados do Usuario ===============")
    print("Nome:", nome)
    print("Data de Nascimento:", data_nasc)
    print("Email:", email)
            
print("============= Cadastro de Usuarios =============")

fim = False

while fim == False:
    nome, data_nasc, email = cad_usuario()
    exib_dados(nome, data_nasc, email)
    fim = True