def dia():
    cantidad = int(input())
    listaDia = []
    for i in range(cantidad):
        temp = int(input())
        presion = int(input())
        pulso = int(input())
        respiracion = int(input())
        listaDia.append((temp, presion, pulso, respiracion))
    return listaDia

def noche():
    cantidad = int(input())
    listaNoche = []
    for i in range(cantidad):
        temp = int(input())
        presion = int(input())
        pulso = int(input())
        respiracion = int(input())
        listaNoche.append((temp, presion, pulso, respiracion))
    return listaNoche

def SalaEstable(listaDia, listaNoche):
    cantidadPacientes = len(listaDia)
    for i in range(cantidadPacientes):
        # Accedemos a la posición [2] de la tupla porque ahí guardamos el pulso
        pulsoD = listaDia[i][2]
        pulsoN = listaNoche[i][2]
        
        # El enunciado pide que la diferencia permitida sea máximo de 1 (igual o casi igual)
        if abs(pulsoD - pulsoN) > 1:
            return False
    return True

#-----------------------------------------------
# Ejecutamos las funciones para llenar los datos
pulsoDia = dia()
pulsoNoche = noche()

print(pulsoDia)
print(pulsoNoche)

# Llamamos a la función con el nombre correcto en mayúscula
if SalaEstable(pulsoDia, pulsoNoche):
    print("La sala está ESTABLE ya que TODOS los pacientes mantuvieron un pulso igual o casi igual entre el día y la noche")
else:
    print("La sala NO está estable, hay pacientes cuyos pulsos variaron más de lo permitido")