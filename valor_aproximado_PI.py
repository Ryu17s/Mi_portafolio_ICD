while True:
    n = int(input())
    if 1 <= n <= 400: break

suma = 0

for i in range(n):
    denominador = (2 * i) + 1
    termino = ((- 1) ** i) / denominador
    suma += termino

pi = 4 * suma
print("pi =",pi)