# Criação da lista de números
numeros = [10, 20, 30, 40, 50]

# Inicialização da variável para armazenar a soma
soma = 0

# Tentativa de calcular a soma dos números
try:
    for numero in numeros:
        soma += numero
    print(f"A soma de todos os elementos é: {soma}")
except TypeError as e:
    print(f"Erro de tipo ao somar os elementos: {e}")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
