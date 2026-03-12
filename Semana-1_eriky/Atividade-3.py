'''
Validar e salvar os dados (nome, data de nascimento, email) em arquivo de texto.
Autor: Eriky R. B. de Medeiro
'''
import pickle

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
    print("\n=============== Cadastro de Usuario ===============")
    nome = ler_nome()
    data_nasc = ler_data_nasc()
    email = ler_email()
    return nome, data_nasc, email

#Funções para salvar e carregar dados.

def salvar_usuario(nome, data_nasc, email):
    with open("usuarios.txt", "a") as arq_usuario:
        arq_usuario.write(f"{nome},{data_nasc},{email}\n")
            
def list_usuario():
    with open("usuarios.txt", "r") as arq_usuario:
        for linha in arq_usuario:
            nome, data_nasc, email = linha.strip().split(",")
            print("\n=============== Dados do Usuario ===============")
            print("Nome:", nome)
            print("Data de Nascimento:", data_nasc)
            print("Email:", email)
            break


if __name__ == "__main__":
    op = -1
    while op != 0:
        op = str(input("Digite uma opção: "))
        match op:
            case "1":
                nome, data_nasc, email = cad_usuario()
                salvar_usuario(nome, data_nasc, email)
            case "2":
                list_usuario()
            case "0":
                print("Encerrando o programa...")
                break
            case _:                    
                print("Opção inválida. Tente novamente.")