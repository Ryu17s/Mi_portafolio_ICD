while True:
    n = int(input())
    if n > 0: break

copia = n
par = 0
impar = 0

while copia > 0:
    digito = copia % 10
    if digito % 2 == 0:
        par += 1
    else:
        impar += 1
    copia //= 10

print("cantidad de digitos pares =",par)
print("cantidad de digitos impares =",impar)

if par == impar:
    print(f"El {n} tiene igual cantidad de digitos pares que impares")
elif par > impar:
    print(f"El {n} tiene mas digitos pares que impares")
else:
    print(f"El {n} tiene mas digitos impares que pares")

    