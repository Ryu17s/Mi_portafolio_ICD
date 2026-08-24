while True:
    n = int(input())
    if n >= 1: break

sumatoria = 0

for i in range(1, n+1):
    sumatoria += (2*i-1)/(2*i)
    
print("El resultado de la sumatoria es",sumatoria)
    