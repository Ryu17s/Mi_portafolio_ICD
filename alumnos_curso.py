def poblar():
    lista = []
    while True:
        n = int(input())
        if n == 0:
            break
        if n > 0:
            lista.append(n)
    return lista

def calcularPromedio(lista):
    return sum(lista) / len(lista)

def contarSobreUmbral(lista, umbral):
    contador = 0
    for n in lista:
        if n > umbral:
            contador += 1
    return contador

def topMayores(lista):
    return sorted(lista, reverse=True)[:3]

def topMenores(lista):
    return sorted(lista)[:3]

def imprimirReporte(lista, umbral):
    maximo = max(lista)
    minimo = min(lista)
    print("REPORTE")
    print("=======")
    print("Lista de cursos =", lista)
    print("Total de cursos =", len(lista))
    print("Total de alumnos =", sum(lista))
    print(f"Promedio de alumnos por curso = {calcularPromedio(lista):.1f}")
    print(f"Valor máximo es {maximo} y se encuenta {lista.count(maximo)} veces")
    print(f"Valor mínimo es {minimo} y se encuenta {lista.count(minimo)} veces")
    print(f"Cantidad de cursos con más alumnos que umbral({umbral}): {contarSobreUmbral(lista, umbral)}")
    print("Top 3 de cursos con más alumnos :", topMayores(lista))
    print("Top 3 de cursos con menos alumnos :", topMenores(lista))

cursos = poblar()

if len(cursos) == 0:
    print("NO HAY CURSOS")
else:
    T = int(input())
    imprimirReporte(cursos, T)