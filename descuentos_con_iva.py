edad = int(input())
cantidad = int(input())
precioSinIVA = float(input())

iva = 1.19

total_IVA = (cantidad * precioSinIVA) * iva

if edad >= 60 and cantidad >= 10:
    porcentaje_descuento = 0.60
else:
    porcentaje_descuento = 0.07

descuento = total_IVA * porcentaje_descuento
totalCompra = total_IVA - descuento

print("Valor Compra con IVA       = $", round(total_IVA, 1))
print("Total Descuento            = $", round(descuento, 1))
print("Valor Compra con Descuento = $", round(totalCompra, 1))