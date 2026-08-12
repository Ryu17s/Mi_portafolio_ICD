altura = float(input())
peso = int(input())
edad = int(input())

imc = peso / altura ** 2

print("imc =",imc,"y edad =",edad)

if imc < 22 and edad < 45:
    print("riesgo cardíaco es bajo")
elif imc < 22 and edad >= 45:
    print("riesgo cardíaco es medio")
elif imc >= 22 and edad < 45:
    print("riesgo cardíaco es medio")
else:
    print("riesgo cardíaco es alto")