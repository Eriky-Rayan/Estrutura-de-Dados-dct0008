dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))
data = f"{dia:02d}/{mes:02d}/{ano}"
print(f"A data digitada foi: {data}")

def format_data(data):
    data = f"{ano}/{mes:02d}/{dia:02d}"
    return data

print(f"A data formatada é: {format_data(data)}")