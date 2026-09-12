n = int(input())
copiaN = n
cont = 0
contCopia = 0 
while copiaN > 0:
    copiaN //= 10
    cont += 1

copiaCopia = n 
sumaPotencia = 0
while copiaCopia > 0:
    digito = copiaCopia % 10
    sumaPotencia += digito ** cont
    copiaCopia //= 10

    
if sumaPotencia == n:
    print(n,"es un numero Armstrong.")
else:
    print(f"{n} no es un numero Armstrong. Suma de potencias: {sumaPotencia}")