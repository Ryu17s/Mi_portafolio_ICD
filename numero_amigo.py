x = int(input())
y = int(input())

amigos_encontrados = 0

for i in range(x, y + 1):
    suma_i = 0
    for m in range(1, i):
        if i % m == 0:
            suma_i += m
            
    if suma_i > i and suma_i <= y:
        suma_j = 0
        for n in range(1, suma_i):
            if suma_i % n == 0:
                suma_j += n
                
        if suma_j == i:
            print(f"{i} y {suma_i}")
            amigos_encontrados += 1

if amigos_encontrados == 0:
    print("no hay amigos en el intervalo")
