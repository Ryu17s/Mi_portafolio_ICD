total = int(input())
descuento = int(input())

montoDescuento = int(total * (descuento / 100))
totalPagar = int(total - montoDescuento)

print("Monto Total Medicamentos =", total)
print(f"Porcentaje de descuento = {descuento}%")
print("Monto de descuento =", montoDescuento)
print("Monto Total a Pagar =", totalPagar)