# Frase de exemplo
frase = "este é um exemplo de frase e este é um teste de frase"

# Dividindo a frase em palavras
palavras = frase.split()

# Inicializando o dicionário para contar a frequência
frequencia_palavras = {}

# Contando a frequência de cada palavra
for palavra in palavras:
    if palavra in frequencia_palavras:
        frequencia_palavras[palavra] += 1
    else:
        frequencia_palavras[palavra] = 1

# Exibindo o resultado
print(frequencia_palavras)
