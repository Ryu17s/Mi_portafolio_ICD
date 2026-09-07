estudiante = int(input())

contA = 0
contR = 0

for i in range(estudiante):
    notaFinal = float(input())
    if notaFinal >= 4.0:
        contA += 1
    else:
        contR += 1

aprobo = (contA / estudiante) * 100
reprobo = (contR / estudiante) * 100

print(f"porcentaje de aprobados = {aprobo} %")
print(f"porcentaje de reprobados = {reprobo} %")