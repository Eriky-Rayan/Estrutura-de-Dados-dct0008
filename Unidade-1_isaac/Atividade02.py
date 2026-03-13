import datetime

Email_valida = 0
Data_valida = 0

Nome = input("Digite o nome: ")

while Email_valida != 1:
    Email = input("Digite o email: ")
    for c in range(len(Email)):
        if Email[c] == '@':
            if '.' not in Email[c:]:
                print("Email inválido! Tente novamente")
            else:
                Email_valida = 1

Senha = input("Digite a senha: ")

while Data_valida != 1:    
    Data_nascimento = input("Digite a data de nascimento (dd/mm/yyyy): ")
    Data_nascimento = datetime.datetime.strptime(Data_nascimento, "%d/%m/%Y")
    if Data_nascimento > datetime.datetime.now():
        print("Data de nascimento inválida! Tente novamente")
    else:
        Data_valida = 1

print("Cadastro realizado com sucesso!")

print(f"O perfil do usuário é: \n{Nome} \n{Email} \n{Senha} \n{Data_nascimento.strftime('%d/%m/%Y')}")