def evaluar_polinomio(coeficientes, x):
    total = 0.0
    potencia_x = 1.0
    for c in coeficientes:
        total = total + c * potencia_x
        potencia_x = potencia_x * x
    return total


n = int(input())

coeficientes = []
for i in range(n):
    coeficientes.append(float(input()))

x = float(input())

resultado = evaluar_polinomio(coeficientes, x)

print(f"Para X = {x:.1f} el polinomio evaluado es igual a {resultado:.1f}")