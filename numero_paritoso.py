n = int(input())
copiaN = n
cont = 0

while copiaN > 0:
    copiaDigito = copiaN % 10
    copiaN //= 10
    if copiaDigito % 2 != 0:
        cont += 1

if n == 0:
    print("Si el número ingresado es 0 es paritoso")
elif cont == 0:
    print(f"Si el número ingresado es {n} es paritoso")
elif n != 0:
    print(f"Si el número ingresado es {n} no es paritoso")