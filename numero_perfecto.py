while True:
    n = int(input())
    if n > 0: break

suma = 0

for i in range(1,n):
    if n % i == 0:
        suma += i

if suma == n:
    print(n,"ES PERFECTO")
else:
    print(n,"NO ES PERFECTO")
    
