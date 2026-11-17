def poblar():
    lista = []
    while True:
        rut = input()
        if rut == "0-0": break
        apellido = input()
        puntaje = int(input())
        lista.append((rut,apellido,puntaje))
    return lista
    
    
def mostrarLista(lista):
    for i in lista:
        print(f"{i[0]} {i[1]} {i[2]}")

def promNotas(lista):
    notas = []
    for i in lista:
        notas.append(i[2])
    if len(notas) == 0:
        return 0
    else:
        prom = round(sum(notas) / len(notas),2)
    return prom
    
def mayorYmenor(lista):
    notas = []
    for i in lista:
        if 0<= i[2] <= 100:
            notas.append(i[2])
    
    if len(notas)> 0:
        menor = min(notas)
        mayor = max(notas)
        print("Menor Calificación =",menor)
        print("Mayor Calificación =",mayor)

def bajoPromedio(lista):
    bajo = []
    prom = promNotas(lista)
    for i in lista:
        if i[2] < prom:
            bajo.append(i[1])
    bajo.sort()
    return bajo

#MAIN

lista = poblar()
promedio = promNotas(lista)
print("LISTA ESTUDIANTES Y PUNTAJE")
print("---------------------------")
mostrarLista(lista)
print("\nPromedio de Calificaciones =",promedio)
mayorYmenor(lista)

bajoCorte = bajoPromedio(lista)
print("\nLISTA DE ESTUDIANTES CON CALIFICACIÓN BAJO EL PROMEDIO")
print("------------------------------------------------------")
if len(bajoCorte) > 0:
    for i in bajoCorte:
        print(i)
else:
    print("--- LISTA VACIA ---")