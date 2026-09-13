n = int(input())
va = abs(n)
ordenado = False

ultimo = va % 10
va //= 10

while va > 0:
    actual = va % 10

    if actual > ultimo:
        ordenado = True
    ultimo = actual
    va //= 10
    
if ordenado == True:
    print(f"El numero {n} NO es ordenado.")
elif ordenado == False:
    print(f"El numero {n} SI es ordenado.")