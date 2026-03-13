texto = "banana"
count = {}

for i in range(len(texto)):
    count[texto[i]] = texto.count(texto[i])
print(count)