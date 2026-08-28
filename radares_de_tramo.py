import math

cantVehiculo = int(input())
while cantVehiculo <= 0:
    cantVehiculo = int(input())

print(f"SE CONTROLARON {cantVehiculo} VEHICULOS\n")

errores = 0
noExcedio = 0
menosGrave = 0
grave = 0
gravisima = 0
utmsRecaudadas = 0.0

for i in range(1, cantVehiculo + 1):
    patente = input().strip()
    distanciaMetros = int(input())
    velMax = int(input())
    segundos = int(input())
    
    print(f"VEHICULO {i} PATENTE {patente}")
    
    if distanciaMetros <= 0 or velMax <= 0 or segundos <= 0:
        print("ERROR EN LOS DATOS REGISTRADOS.\n")
        errores += 1
    else:
        velMediaReal = (distanciaMetros * 3.6) / segundos
        velMedia = math.trunc(velMediaReal)
        
        print(f"Velocidad Máxima Permitida en el Tramo = {velMax}")
        print(f"Velocidad Media Vehículo = {velMedia}")
        
        if velMedia <= velMax:
            print("No excedió velocidad máxima permitida.\n")
            noExcedio += 1
        else:
            exceso = velMedia - velMax
            print(f"Excedió velocidad máxima permitida en {exceso} kms/h.")
            
            if exceso <= 10:
                print("FALTA : Menos Grave - SANCIÓN : 1 UTM.\n")
                menosGrave += 1
                utmsRecaudadas += 1.0
            elif exceso <= 20:
                print("FALTA : Grave - SANCIÓN : 1.5 UTM.\n")
                grave += 1
                utmsRecaudadas += 1.5
            else:
                print("FALTA : Gravísima - SANCIÓN : 3 UTM y se SUSPENDE LICENCIA 45 días.\n")
                gravisima += 1
                utmsRecaudadas += 3.0

print("********** REPORTE FINAL **********\n")

pctErrores = (errores / cantVehiculo) * 100
pctNoExcedio = (noExcedio / cantVehiculo) * 100
pctMenosGrave = (menosGrave / cantVehiculo) * 100
pctGrave = (grave / cantVehiculo) * 100
pctGravisima = (gravisima / cantVehiculo) * 100

print(f"El {pctErrores:.1f} % presentó un error en el registro de datos.")
print(f"El {pctNoExcedio:.1f} % NO iba a exceso de velocidad.")
print(f"El {pctMenosGrave:.1f} % cometió una falta menos grave.")
print(f"El {pctGrave:.1f} % cometió una falta grave.")
print(f"El {pctGravisima:.1f} % cometió una falta gravísima.\n")

if utmsRecaudadas.is_integer():
    print(f"Se recaudaron {int(utmsRecaudadas)} UTMs.")
else:
    print(f"Se recaudaron {utmsRecaudadas} UTMs.")

print("\n*********** FIN REPORTE ************")