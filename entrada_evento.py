montoUF = int(input())
opcion = int(input())
entrada = int(input())

dolar = 845

if opcion == 1 and montoUF >= 1 and montoUF <= 99:
    descuento = "8 %"
    precioDolar = entrada * (1 - 0.08)

elif opcion == 1 and montoUF >= 100:
    descuento = "30 %"
    precioDolar = entrada * (1 - 0.30)

elif opcion == 2 and montoUF >= 1 and montoUF <= 99:
    descuento = "25 %"
    precioDolar = entrada * (1 - 0.25)

elif opcion == 2 and montoUF >= 100:
    descuento = "45 %"
    precioDolar = entrada * (1 - 0.45)

precioPesos = precioDolar * dolar

print(f"Tienes un descuento del {descuento}")
print(f"El valor final de tu entrada en dólares es {precioDolar}")
print(f"El valor final de tu entrada en pesos es {precioPesos}")
