peso = float(input())
altura = float(input())

imc = round(peso / (altura ** 2), 1)

print("imc paciente =",imc)
if imc < 16.5 or imc >= 25:
    print("Alerta : paciente debe modificar su dieta alimenticia")
else:
    print("Alerta : paciente debe mantener su dieta alimenticia.")