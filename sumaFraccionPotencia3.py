sumatoria = 0

while True:
    n = int(input())
    if 1 <= n <= 14: break

for i in range(1,n+1):
    sumatoria += 1 / (3 ** (i - 1))

print(f"La suma de {n}  terminos es {sumatoria}")