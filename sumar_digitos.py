n = int(input())
copiaN = n
cont = 0

while copiaN > 0:
    copiaDigito = copiaN % 10
    copiaN //= 10
    cont += copiaDigito

if n == 0:
    print(f"Si el número ingresado es {n} la suma de sus dígitos es 0")
else:
    print(f"Si el número ingresado es {n} la suma de sus dígitos es {cont}")