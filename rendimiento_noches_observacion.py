totalDatosAprovechables = 0
totalHorasPerdidas = 0
totalNoches = 0
contOptimas = 0
totalRadio = 0
sumaRadio = 0
contCieloMalo = 0
contMaloPerdida = 0
maxDatosAprovechables = -1
maxPrograma = ""

while True:
    noches = int(input())
    if noches >= 1 and noches <= 365: break
print("Noches a procesar:",noches,"\n")
    
for i in range(noches):
    nombre = input()
    instrumento = int(input())
    horas = float(input())
    nubosidad = float(input())
    calidadCielo = int(input())
    horasPerdidas = nubosidad
    horasEfectivas = horas - horasPerdidas
    eficienciaNoche = (horasEfectivas / horas) * 100
    
    if instrumento == 1:
        tasaGeneracion = 40
    elif instrumento == 2:
        tasaGeneracion = 75
    elif instrumento == 3:
            tasaGeneracion = 220
    datosGB = horasEfectivas * tasaGeneracion
    
    if calidadCielo == 1:
        factor = 1
    elif calidadCielo == 2:
        factor = 0.85
    elif calidadCielo == 3:
        factor = 0.60
    datosAprovechables = datosGB * factor
    
    if eficienciaNoche >= 90 and calidadCielo == 1:
        rendimiento = "ÓPTIMA"
    elif eficienciaNoche >= 70:
        rendimiento = "ÚTIL"
    else:
        rendimiento = "PERDIDA"
        
    totalDatosAprovechables += datosAprovechables 
    totalHorasPerdidas += horasPerdidas
    totalNoches += 1
    
    if rendimiento == "ÓPTIMA":
        contOptimas += 1
    
    if instrumento == 3:
        totalRadio += 1
        sumaRadio += eficienciaNoche
    
    if calidadCielo == 3:
        contCieloMalo += 1
        if rendimiento == "PERDIDA":
            contMaloPerdida += 1
    
    if datosAprovechables > maxDatosAprovechables:
        maxDatosAprovechables = datosAprovechables
        maxPrograma = nombre
    
    print("Programa:",nombre)
    print("Efectivas:",round(horasEfectivas,2))
    print(f"Eficiencia: {round(eficienciaNoche,2)} %")
    print("Datos:",round(datosAprovechables,2))
    print("Noche:",rendimiento,"\n")
    
porcentajeNocheOptima = (contOptimas * 100) / noches

print("Total datos:",round(totalDatosAprovechables,2))
print(f"Noches óptimas: {round(porcentajeNocheOptima,1)} %")

if totalRadio > 0:
    promedioRadio = round(sumaRadio / totalRadio,2)
    print("Promedio radio:",promedioRadio)
else:
    print("Sin radiotelescopio")
    
if contCieloMalo > 0:
    perdidasCieloMalo = (contMaloPerdida * 100 ) / contCieloMalo 
    print(f"Perdidas cielo malo: {round(perdidasCieloMalo,1)} %")
else:
    print("Sin cielo malo")

print(f"Mayor datos: {maxPrograma} {round(maxDatosAprovechables,2)}")
print("Horas perdidas:",round(totalHorasPerdidas,2))