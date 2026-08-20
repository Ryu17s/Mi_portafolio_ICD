cargoFijo = float(input())
litrosConsumidos = float(input())
valorM3 = float(input())
cargoRecoleccion = float(input())
cargoTratamiento = float(input())
m3Consumido = litrosConsumidos / 1000
pagarAgua = m3Consumido * valorM3

cargoPotable = litrosConsumidos * valorM3

totalRecoleccion = m3Consumido * cargoRecoleccion
totalTratamiento = m3Consumido * cargoTratamiento
variableAlcantarillado = totalRecoleccion + totalTratamiento

montoBase = cargoFijo + pagarAgua + variableAlcantarillado

print("BOLETA ESVALPITO")
print(f"Cargo Fijo = ${cargoFijo}")
print("Metros cúbicos de agua consumidos =", m3Consumido)
print(f"Monto parcial por agua consumida = ${pagarAgua}")
print(f"Monto parcial por agua recolectada = ${totalRecoleccion}")
print(f"Monto parcial por agua tratada = ${totalTratamiento}")

if m3Consumido >= 40 and m3Consumido < 45:
    print("Cliente presenta sobreconsumo, su recargo es de un 15%")
    print(f"Monto Total Antes del recargo = ${montoBase}") 
    totalPagar = montoBase * 1.15
elif m3Consumido >= 45 and m3Consumido < 50:
    print("Cliente presenta sobreconsumo, su recargo es de un 20%")
    print(f"Monto Total Antes del recargo = ${montoBase}")
    totalPagar = montoBase * 1.20
elif m3Consumido >= 50 and m3Consumido < 65:
    print("Cliente presenta sobreconsumo, su recargo es de un 30%")
    print(f"Monto Total Antes del recargo = ${montoBase}")
    totalPagar = montoBase * 1.30
elif m3Consumido >= 65:
    print("Cliente presenta sobreconsumo, su recargo es de un 55%")
    print(f"Monto Total Antes del recargo = ${montoBase}")
    totalPagar = montoBase * 1.55
else:
    print("Cliente no presenta sobreconsumo")
    totalPagar = montoBase

print(f"Monto Total a Pagar = ${totalPagar}") 