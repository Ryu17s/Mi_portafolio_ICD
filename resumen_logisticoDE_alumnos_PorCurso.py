# definicion de funciones

def leerAlumnos():
    listaCursos = []
    while True:
        cantAlumnos = int(input("Valor: "))
        if cantAlumnos == 0:
            break
        if cantAlumnos > 0:
            listaCursos.append(cantAlumnos)
    return listaCursos
    
def umbral():
    while True: 
        t = int(input("Valor: "))
        if t >= 0:
            return t

def estadisticas(listaCursos, umbralT):
    totalCursos = len(listaCursos)
    totalAlumnos = sum(listaCursos)
    prom = totalAlumnos / totalCursos
    promRound = round(prom,1)

    valmax =  max(listaCursos)
    repemax = listaCursos.count(valmax)

    valmin = min(listaCursos)
    repemin = listaCursos.count(valmin)
    
    superanT = 0
    for curso in listaCursos:
        if curso > umbralT:
            superanT += 1
    
    listaOrdenada = sorted(listaCursos)
    top3Menos = listaOrdenada[:3]
    top3Mas = listaOrdenada[-3:][::-1]
    return (totalCursos, totalAlumnos, promRound, valmax, repemax, valmin, repemin, superanT, top3Mas, top3Menos)
 
# programa principal

cursosInscritos = leerAlumnos()
if len(cursosInscritos) == 0:
    print("NO HAY CURSOS")
else:
    valorUmbral = umbral()
    
    totalCursos, totalAlumnos, promRound, valmax, repemax, valmin, repemin, superanT, top3Mas, top3Menos = estadisticas(cursosInscritos, valorUmbral)

    print("REPORTE")
    print("=======")
    print(f"Lista de cursos = {cursosInscritos}")
    print(f"Total de cursos = {totalCursos}")
    print(f"Total de alumnos = {totalAlumnos}")
    print(f"Promedio de alumnos por curso = {promRound}")
    print(f"Valor máximo es {valmax} y se encuenta {repemax} veces")
    print(f"Valor mínimo es {valmin} y se encuenta {repemin} veces")
    print(f"Cantidad de cursos con más alumnos que umbral({valorUmbral}): {superanT} ")
    print(f"Top 3 de cursos con más alumnos : {top3Mas}")
    print(f"Top 3 de cursos con menos alumnos : {top3Menos}")
    
    
    




