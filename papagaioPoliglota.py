# Bootcamp "Geração Tech Unimed-BH - Ciência de Dados"
# Digital Innovation One
# Desafios Intermediários Py: Papagaio Poliglota

while True: 
    try:
        # entrada de dados
        entrada = input()
        entrada = entrada.split()
        
        # avalia a posição das pernas do papagaio e retorna a língua
        for i in entrada:
            if i == "esquerda":
                print("ingles")
            elif i == "direita":
                print("frances")
            elif i == "nenhuma":
                print("portugues")
            elif i == "ambas":
                print("caiu")
    except EOFError: # saiu do programa com CTRL+D
        break