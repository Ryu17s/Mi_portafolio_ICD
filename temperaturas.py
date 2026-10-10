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
    print(f"Las {len(lista)} temperaturas son :",end=" ")
    for elemento in lista:
        print(elemento,end=" ")
    print()

    
dias = validar()
lista = poblarLista(dias)
promedio = (sum(lista) / dias)
mostrar(lista)

print(f"\nTemperatura mínima es {min(lista)}")
print(f"Temperatura máxima es {max(lista)}")
print(f"Promedio de {dias} temperaturas es {promedio:.2f}")

sobreProm = 0
for temp in lista:
    if temp > promedio:
        sobreProm +=1
print("Cantidad de mediciones sobre el promedio es",sobreProm)