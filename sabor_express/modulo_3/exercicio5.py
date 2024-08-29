# Solicitando um número ao usuário
numero = int(input("Digite um número para ver a tabuada: "))

# Usando um loop for para imprimir a tabuada de 1 a 10
print(f"Tabuada do {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
