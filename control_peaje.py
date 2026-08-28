totalRecaudado = 0
totalVehiculos = 0
tarifaMaxima = 0


while True:
    tipo = int(input("ingrese: "))
    if tipo == 0:
        break
    if tipo == 1:
        tarifaBase = 1500
    elif tipo == 2:
        tarifaBase = 3000
    elif tipo == 3:
        tarifaBase = 6000
    else:
        print("No valido")
        continue

    horaPico = int(input("ingrese: "))

    if horaPico == 1:
        tarifaFinal = tarifaBase * 1.20
    else:
        tarifaFinal = tarifaBase

    totalVehiculos += 1
    totalRecaudado += tarifaFinal

    if tarifaFinal > tarifaMaxima:
        tarifaMaxima = tarifaFinal    

# Resultados    
print("_-_-_-_-Resultados-_-_-_-_")
print("El total de vehículos registrados es",totalVehiculos )
print("El total de dinero recaudado es", totalRecaudado)
print("La tarifa individual más alta registrada es", tarifaMaxima)
