# Bootcamp "Geração Tech Unimed-BH - Ciência de Dados"
# Digital Innovation One
# Desafio de Código: As Duas Torres

# Dados de entrada na ordem N, X e Y, separados por espaços
entrada = input("Digite os valores de entrada, separados por espaços: ").split()

# a distância entre os Palantír - N(0 < N < 10000)
N = int(entrada[0])

# o diâmetro do Palantír de Sauron - X > 0
X = int(entrada[1])

#  o diâmetro do Palantír de Saruman - Y < 100
Y = int(entrada[2])

# Cálculo do ICM
ICM = N / (X + Y)

print("%.2f" %ICM)