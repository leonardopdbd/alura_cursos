# Defina o nome de usuário e a senha esperados
nome_usuario_esperado = "admin"
senha_esperada = "12345"

# Solicita ao usuário que insira o nome de usuário e a senha
nome_usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

# Verifica se o nome de usuário e a senha correspondem aos valores esperados
if nome_usuario == nome_usuario_esperado and senha == senha_esperada:
    print("Login bem-sucedido!")
else:
    print("Nome de usuário ou senha incorretos.")
