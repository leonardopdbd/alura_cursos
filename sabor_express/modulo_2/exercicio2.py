# Solicita ao usuário que insira sua idade
idade = int(input("Digite sua idade: "))

# Classifica a idade em categorias
if idade >= 0 and idade <= 12:
    print("Você é uma criança.")
elif idade >= 13 and idade <= 18:
    print("Você é um adolescente.")
elif idade > 18:
    print("Você é um adulto.")
else:
    print("Idade inválida.")
