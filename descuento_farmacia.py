monto_total = int(input("Monto Total Medicamentos"))
porcentaje_descuento = int(input("Porcentaje de descuento"))

monto_descuento = (monto_total * porcentaje_descuento) / 100
total_pagar = monto_total - monto_descuento

print(f"Monto Total Medicamentos = {monto_total}")
print(f"Porcentaje de descuento = {porcentaje_descuento}%")
print(f"Monto de descuento = {int(monto_descuento)}")
print(f"Monto Total a Pagar = {int(total_pagar)}")