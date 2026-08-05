# Julián Erazo Munoz
# Rut: 22422798-1
# Curso ICD 1341-1

# Analisis del problema

# Datos de entrada

# n (int): Cantidad total de misiones a registrar.
# nombreRobot (str) : Nombre del robot que realiza la misión.
# sede (str): Sede donde se realiza la misión.
# tipoMision (str): Tipo de misión realizada.
# duracion (int): Duración de la misión en minutos.
# porcentajeBateria (int): Porcentaje de batería consumida  durante la misión.
# prioridadMision (int): Nivel de prioridad de la misión (1 al 5).
# sedeAct (str): Sede a consultar en el reporte final.
# tipoMisionAct (str): Tipo de misión a consultar en el reporte final.
# prioridadMinAct (int): Prioridad mínima a consultar.
# robotAct (str): Nombre del robot a consultar.
# limiteBateriaAct (int): Límite de batería mínimo a consultar.

# DATOS DE SALIDA:

# cantSede (int): Cantidad de misiones en la sede consultada.
# batTotalTodos (int): Suma total de batería utilizada por todos los robot.
# promedioDuracionTipo (float): Promedio de duración de las misiones del tipo consultado.
# robotMaxBat (str): Nombre del robot con el mayor consumo de batería.
# cantPrioMin (int): Cantidad de misiones con prioridad mayor o igual a la consultada.
# cantRobotAct (int): Cantidad de misiones realizadas por el robot consultado.
# duracionRobotAct (int): Duración total de las misiones del robot consultado.
# cantCriticas (int): Cantidad total de misiones criticas registradas.
# cantEficientes (int): Cantidad total de misiones eficientes registradas.
# cantLimiteBat (int): Cantidad de misiones que superan o igualan el límite de batería.
# destacado (bool): Indica si el robot consultado es destacado.



# Definicion de funciones

# Evalua si la mision cumple con al menos una condición para ser catalogada como critica
def esCritica(prioridad,duracion,bateria):
    return prioridad == 5 or duracion >= 40 or bateria >= 20

# Evalúa si la misión cumple las condiciones para ser eficiente
def esEficiente(duracion,bateria):
    return duracion <= 25 and bateria <= 12

# Verifica si el robot cumple los requisitos de actividad
def robotDestacado(cantidad,duracion):
    return cantidad >= 2 and duracion >= 40

# Evalua la lista de misiones para encontrar al robot con mayor gasto de batería    
def mayorConsumo(listaMisiones):
    maxBateria = -1
    nombreMax = ""
    for mision in listaMisiones:
        if mision[4] > maxBateria:
            maxBateria = mision[4]
            nombreMax = mision[0]
    return nombreMax
    
# Programa principal

# Registro de datos de misiones
n = int(input())
misiones = []

for i in range(n):
    nombreRobot = input().strip().upper()
    sede = input().strip().upper()
    tipoMision = input().strip().upper()
    duracion = int(input().strip())
    porcentajeBateria = int(input().strip())
    prioridadMision = int(input().strip())
    
    misiones.append((nombreRobot, sede, tipoMision, duracion, porcentajeBateria, prioridadMision))
    
sedeAct = input().strip().upper()
tipoMisionAct = input().strip().upper()
prioridadMinAct = int(input().strip())
robotAct = input().strip().upper()
limiteBateriaAct = int(input().strip())

# Inicio de contadores
cantSede = 0
batTotalTodos = 0
duracionTipo = 0
cantTipo = 0
cantPrioMin = 0
cantRobotAct = 0
duracionRobotAct = 0
cantCriticas = 0
cantEficientes = 0
cantLimiteBat = 0

# Procesamiento de datos de las misiones
for mision in misiones:
    m_nombre, m_sede, m_tipo, m_duracion, m_bateria, m_prioridad = mision
    
    if m_sede == sedeAct:
        cantSede += 1
        
    batTotalTodos += m_bateria
    
    if m_tipo == tipoMisionAct:
        duracionTipo += m_duracion
        cantTipo += 1
        
    if m_prioridad >= prioridadMinAct:
        cantPrioMin += 1
        
    if m_nombre == robotAct:
        cantRobotAct += 1
        duracionRobotAct += m_duracion
        
    if esCritica(m_prioridad, m_duracion, m_bateria):
        cantCriticas += 1
        
    if esEficiente(m_duracion, m_bateria):
        cantEficientes += 1
        
    if m_bateria >= limiteBateriaAct:
        cantLimiteBat += 1
 
if cantTipo > 0:
    promedioDuracionTipo = duracionTipo / cantTipo
else:
    promedioDuracionTipo = 0.0

robotMaxBat = mayorConsumo(misiones)
destacado = robotDestacado(cantRobotAct, duracionRobotAct)

# reporte final
print("REPORTE DE MISIONES ROBÓTICAS PUCV")
print()
print(f"Misiones realizadas en {sedeAct}: {cantSede}")
print(f"Batería total utilizada: {batTotalTodos}")
print(f"Promedio de duración en misiones de tipo {tipoMisionAct}: {promedioDuracionTipo:.1f}")
print(f"Robot con mayor consumo de batería en una misión: {robotMaxBat}")
print(f"Misiones con prioridad mayor o igual a {prioridadMinAct}: {cantPrioMin}")
print(f"Misiones realizadas por {robotAct}: {cantRobotAct}")
print(f"Duración total de misiones realizadas por {robotAct}: {duracionRobotAct}")
print(f"Misiones críticas: {cantCriticas}")
print(f"Misiones eficientes: {cantEficientes}")
print(f"Misiones con batería mayor o igual a {limiteBateriaAct}: {cantLimiteBat}")

if destacado:
    print(f"{robotAct} es un robot destacado")
else:
    print(f"{robotAct} no es un robot destacado")