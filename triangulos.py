n = int(input("Ingrese longitud"))
while not 1 < n < 21:
    n = int(input())

for i in range(n):
    for j in range(i):
        print(" ", end="")
    for k in range(n - i):
        print("* ", end="")
    print()

for i in range(1, n):
    for j in range(n - 1 - i):
        print(" ", end="")
    for k in range(i + 1):
        print("* ", end="")
    print()