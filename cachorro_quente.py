# Bootcamp "Geração Tech Unimed-BH - Ciência de Dados"
# Digital Innovation One
# Desafio de Código: Competição de Cachorros-Quentes do Nathan

# Dados de entrada na ordem H e P, separados por espaços
valores = input("Digite os valores de entrada, separados por espaços: ").split()

# número total de cachorros-quentes consumidos - H >= 1
H = int(valores[0])

# número total de participantes na competição - P <= 1000
P = int(valores[1])

avgHotDog = H / P

print("%.2f" %avgHotDog)