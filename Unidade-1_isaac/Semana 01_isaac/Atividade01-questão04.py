numeros = []

def min_max(numeros):
    min_value = numeros[0]
    max_value = numeros[0]

    for num in numeros:
        if num < min_value:
            min_value = num
        elif num > max_value:
            max_value = num

    return (min_value, max_value)

q = int(input("Digite a quantidade de números: "))
for i in range(q):
    n = int(input(f"Digite o número {i + 1}: "))
    numeros.append(n)

min_max(numeros)

print(f"O menor número é: {min_max(numeros)[0]}")
print(f"O maior número é: {min_max(numeros)[1]}")