unidad = int(input())
pack = int(input())
precioUnitario = float(input())

totalLatas = unidad + (pack * 6)
montoTotal = totalLatas * precioUnitario

descuento = 0

if pack >= 10:
    if montoTotal >= 30000 and montoTotal < 50000:
        descuento = montoTotal * 0.1
    elif montoTotal >= 50000 and montoTotal < 70000:
        descuento = montoTotal * 0.15
    elif montoTotal >= 70000:
        descuento = montoTotal * 0.20

totalPagar = montoTotal - descuento

print("Total de la compra = $",round(montoTotal))
print("Descuento = $",round(descuento))
print("Precio total a pagar = $",round(totalPagar))
