# Definicion de funciones
def validarPatente():
    n = int(input("Ingrese valor de la patente: "))
    if n < 9000 and n % 2 == 0:
        return True
    return False
        
def verificarVelocidad():
    vel = int(input("Ingrese velocidad: "))
    if vel <= 50:
        return True
    return False

def evaluarConductor():
    edad = int(input("Ingrese edad: "))
    if edad >= 18 and '4' not in str(edad):
        return True
    return False

# Programa principal

totalVehiculos = 0
vehiculosAprobados = 0

while True:
    print("--- NUEVO VEHÍCULO ---")
    
    patenteValida = validarPatente()
    velocidadValida = verificarVelocidad()
    conductorValido = evaluarConductor()
    
    totalVehiculos += 1
    
    # Verificamos si cumple con TODAS las condiciones
    if patenteValida and velocidadValida and conductorValido:
        print("Resultado: Vehículo y conductor APROBADOS.")
        vehiculosAprobados += 1
    else:
        print("Resultado: Vehículo o conductor RECHAZADOS.")

# Estadisticas finales

print("=============================================")
print("             ESTADÍSTICAS FINALES            ")
print("=============================================")
print(f"El total de vehículos ingresados es: {totalVehiculos}")
print(f"El total de vehículos aprobados es: {vehiculosAprobados}")
print("=============================================")