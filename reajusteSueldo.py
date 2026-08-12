salario = float(input())

if salario < 250000:
    reajuste = salario * 1.2
elif salario >= 250000 and salario < 500000:
    reajuste = salario * 1.1
elif salario >= 500000 and salario < 1000000:
    reajuste = salario * 1.05
else:
    reajuste = salario

print("Salario reajustado = $", round(reajuste))
