# Solicita ao usuário que insira as coordenadas (x, y)
x = float(input("Digite a coordenada x: "))
y = float(input("Digite a coordenada y: "))

# Determina em qual quadrante o ponto se encontra
if x > 0 and y > 0:
    print("O ponto está no Primeiro Quadrante.")
elif x < 0 and y > 0:
    print("O ponto está no Segundo Quadrante.")
elif x < 0 and y < 0:
    print("O ponto está no Terceiro Quadrante.")
elif x > 0 and y < 0:
    print("O ponto está no Quarto Quadrante.")
else:
    print("O ponto está localizado no eixo ou na origem.")
