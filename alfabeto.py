# Bootcamp "Geração Tech Unimed-BH - Ciência de Dados"
# Digital Innovation One
# Desafios Intermediários Py: Alfabeto

# função para transformar a letra em ascii e determinar a posição noalfabeto
def letterPosition(letra):
    letra = letra.lower()
    return ord(letra)-96

# dados de entrada
letra = input()

# imprime a posição da letra    
print(letterPosition(letra))