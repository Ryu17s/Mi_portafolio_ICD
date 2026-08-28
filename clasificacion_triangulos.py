a = float(input())
b = float(input())
c = float(input())

if (a + b > c) and (a + c > b) and (c + b > a):
    print("Si es un triángulo")

    if a == b and b == c:
        print("El triángulo es equilátero")
    elif a == b or b == c or a == c:
        print("El triángulo es isósceles")
    elif a != b and b != c:
        print("El triángulo es escaleno")
else:
    print("No es un triángulo.")


