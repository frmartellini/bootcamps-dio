# Bootcamp "Geração Tech Unimed-BH - Ciência de Dados"
# Digital Innovation One
# Desafios Intermediários Py: Aumento Salarial

salario = float(input()) 

if (600 >= salario >= 0):
    print("Novo salario: %.2f" %(salario*1.17))
    print("Reajuste ganho: %.2f" %(salario*0.17))
    print("Em percentual: 17 %")
elif (900 >= salario >= 600.01):
    print("Novo salario: %.2f" %(salario*1.13))
    print("Reajuste ganho: %.2f" %(salario*0.13))
    print("Em percentual: 13 %")
elif (1500 >= salario >= 900.01):
    print("Novo salario: %.2f" %(salario*1.12))
    print("Reajuste ganho: %.2f" %(salario*0.12))
    print("Em percentual: 12 %")
elif (2000 >= salario >= 1500.01):
    print("Novo salario: %.2f" %(salario*1.10))
    print("Reajuste ganho: %.2f" %(salario*0.10))
    print("Em percentual: 10 %")
else:
    print("Novo salario: %.2f" %(salario*1.05))
    print("Reajuste ganho: %.2f" %(salario*0.05))
    print("Em percentual: 5 %")