a = int(input())
b = int(input())
suma = 0

for i in range(a, b+1):
    suma += i**2
    
print(f"La suma de cuadrados entre {a} y {b} es {suma}")