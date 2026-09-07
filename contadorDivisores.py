n = int(input())
cont = 0

if n < 0:
    limite = -n
else:
    limite = n
    
for i in range(1,limite+1):
    if limite % i == 0:
        cont += 1 

if n == 0:
    print("El 0 tiene infinitos divisores")
elif cont > 0:
    print(f"El {n} tiene {cont} divisores positivos")