capital_invertido = float(input("Capital: "))
tasa_mensual = float(input("Tasa: "))

ganancia = capital_invertido * (tasa_mensual / 100)
capital_actualizado = capital_invertido + ganancia

print(f"Monto de dinero invertido = {int(capital_invertido)}")
print(f"Tasa de interés mensual = {int(tasa_mensual)}%")
print(f"Monto de dinero que ganará el inversionista = {int(ganancia)}")
print(f"Capital actualizado es {int(capital_actualizado)}")