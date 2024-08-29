# Criação da lista de números
numeros = [10, 20, 30, 40, 50]

# Tentativa de calcular a média dos números
try:
    # Verifica se a lista está vazia
    if len(numeros) == 0:
        raise ZeroDivisionError("A lista está vazia. Não é possível calcular a média.")

    # Calcula a soma dos elementos da lista
    soma = sum(numeros)
    
    # Calcula a média
    media = soma / len(numeros)
    
    print(f"A média dos valores na lista é: {media}")
    
except ZeroDivisionError as e:
    print(f"Erro: {e}")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
