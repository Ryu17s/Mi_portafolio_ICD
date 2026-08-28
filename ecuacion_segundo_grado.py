a = float(input())
b = float(input())
c = float(input())


d = b ** 2 - 4 * a * c

if a == 0:
    print("No es una ecuación de segundo grado")
else: 
    if d > 0:
        x1 = round((-b + (d ** 0.5)) / (2 * a),1)
        x2 = round((-b - (d ** 0.5)) / (2 * a),1)
        print("x1 =",x1)
        print("x2 =",x2)
    
    elif d == 0:
        x = -b / (2 * a)
        print(f"x = {x}")

    else:
        print("La ecuación tiene raíces complejas.")