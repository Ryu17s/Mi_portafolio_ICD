total = 0
maxima = 0
minima = 0

while True:
    temp = float(input("Ingrese tempereatura: "))
    if temp == -99:
        break

    if temp < 10:
        print("Alerta: Encendiendo calefaccion")
    elif temp >= 10 and temp <= 25:
        print("Estado: Temperatura optima")
    else:
        print("Alerta: Activando ventiladores")

    total += 1

    if total == 1:
        maxima = temp
        minima = temp
    else:
        if temp > maxima:
            maxima = temp
        if temp < minima:
            minima = temp
# Estadisticas
print("-----------------------------------")
print("El total de lecturas procesadas es", total )
print("Temperatura maxima es", maxima)
print("Temperatura minima es" , minima)