# Dicionário original com as informações da pessoa
pessoa = {
    'nome': 'Carlos Almeida',
    'idade': 30,
    'cidade': 'São Paulo'
}

# 1. Modificando o valor de um dos itens (atualizando a idade da pessoa)
pessoa['idade'] = 31

# 2. Adicionando um campo de profissão para essa pessoa
pessoa['profissao'] = 'Engenheiro de Software'

# 3. Removendo um item do dicionário (removendo a cidade)
del pessoa['cidade']

# Exibindo o dicionário final após as modificações
print(pessoa)
