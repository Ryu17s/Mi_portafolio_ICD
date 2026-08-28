catedra1 = float(input())
catedra2 = float(input())
catedra3 = float(input())

promedio = round((catedra1 + catedra2 + catedra3) / 3, 2)

print("promedio =", promedio)

if promedio < 3:
    print("Reprobaste la asignatura")
elif promedio >= 6.5:
    print("Aprobaste la asignatura")
else:
    print("Debes rendir examen final en esta asignatura")