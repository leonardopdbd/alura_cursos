# Inicializando a variável que armazenará a soma
soma_impares = 0

# Usando um loop for para percorrer os números de 1 a 10
for numero in range(1, 11):
    # Verificando se o número é ímpar
    if numero % 2 != 0:
        soma_impares += numero

# Imprimindo a soma dos números ímpares
print("A soma dos números ímpares de 1 a 10 é:", soma_impares)
