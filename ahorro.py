capital = float(input())
interes = float(input())
interesDecimal = interes / 100

ganancia = capital * interesDecimal
capitalActualizado = capital + ganancia

print(f"Monto de dinero invertido = {int(capital)}")
print(f"Tasa de interés mensual = {int(interes)}%")
print(f"Monto de dinero que ganará el inversionista = {int(ganancia)}")
print(f"Capital actualizado = {int(capitalActualizado)}")