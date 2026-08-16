edad = int(input())
destino = int(input())
valorPasaje = int(input())

dolar = 749

if edad <= 30 and destino == 1:
    porcentaje = 15
    valorFinal = valorPasaje * 0.85
elif edad <= 30 and destino == 2:
    porcentaje = 5
    valorFinal = valorPasaje * 0.95
elif edad >= 31 and destino == 1:
    porcentaje = 20
    valorFinal = valorPasaje * 0.80
elif edad >= 31 and destino == 2:
    porcentaje = 10
    valorFinal = valorPasaje * 0.90

pesos = valorFinal * dolar

print(f"Tienes un descuento del {porcentaje} %")
print("El valor final de tu pasaje en dólares es", valorFinal)
print("El valor final de tu pasaje en pesos es", pesos)