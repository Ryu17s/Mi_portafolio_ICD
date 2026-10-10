def validar():
    while True:
        n = int(input())
        if 1 <= n <= 365:
            return n


def poblarLista(n):
    lista = []
    for i in range(n):
        lista.append(float(input()))
    return lista


def mostrar(lista):
    print(f"Las {len(lista)} temperaturas son :", end=" ")
    for elemento in lista:
        print(elemento, end=" ")
    print()


def sumar(lista):
    total = 0
    for t in lista:
        total += t
    return total


def sobrePromedio(lista, prom):
    cont = 0
    for t in lista:
        if t > prom:
            cont += 1
    return cont


dias = validar()
lista = poblarLista(dias)
promedio = sumar(lista) / dias

mostrar(lista)
print(f"\nTemperatura mínima es {min(lista)}")
print(f"Temperatura máxima es {max(lista)}")
print(f"Promedio de {dias} temperaturas es {round(promedio, 2)}")
print(f"Cantidad de mediciones sobre el promedio es {sobrePromedio(lista, promedio)}")