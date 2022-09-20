# Bootcamp "Geração Tech Unimed-BH - Ciência de Dados"
# Digital Innovation One
# Desafio de Código: Viagem de Carro do Rubens

# Dados de entrada na ordem Tempo e Velocidade Média, separados por espaços
valores = input("Digite os valores de entrada, separados por espaços: ").split()

# tempo gasto na viagem em horas 
tempo = int(valores[0])

# velocidade média durante a mesma em km/h
velocidade_media = int(valores[1])

# cálculo do consumo de combustível
combustivel = (tempo * velocidade_media) / 12

print("%.3f" %combustivel)