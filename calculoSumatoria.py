while True:
    n = int( input())
    if n > 0: break

contador = 0
for i in range(1, n + 1):
    contador += i
    
print(f"Sumatoria de 1 a {i} = {contador}")