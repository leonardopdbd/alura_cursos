# Criando um dicionário de exemplo
dados_pessoais = {
    'nome': 'Joana Gabriela',
    'idade': 28,
    'cidade': 'Rio de Janeiro'
}

# Verificando se uma chave específica existe no dicionário
chave_a_verificar = 'idade'

if chave_a_verificar in dados_pessoais:
    print(f"A chave '{chave_a_verificar}' existe no dicionário.")
else:
    print(f"A chave '{chave_a_verificar}' não existe no dicionário.")
