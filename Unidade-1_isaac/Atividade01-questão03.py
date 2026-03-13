def calcula_salario(valor_hora, horas_normais, horas_extras):
    valor_hora = float(input("Digite o valor da hora: "))
    horas_normais = float(input("Digite a quantidade de horas normais trabalhadas: "))
    horas_extras = float(input("Digite a quantidade de horas extras trabalhadas: "))
    salario_normal = valor_hora * horas_normais
    salario_extra = valor_hora * 1.5 * horas_extras
    salario_total = salario_normal + salario_extra
    print(f"O salário total é: R${salario_total:.2f}")
    