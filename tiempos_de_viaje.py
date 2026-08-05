tramos = int(input("Ingrene tramos"))
while tramos <= 0:
    tramos = int(input("Ingrese tramos"))

totalJuan = 0
totalMario = 0

for i in range(tramos):
    tiempoMario = int(input("Ingrese tiempo"))
    tiempoJuan = int(input("Ingrese tiempo"))
    
    totalMario += tiempoMario
    totalJuan += tiempoJuan
    
if totalJuan > totalMario:
    print(f"Mario ha ganado con un total de {totalMario} minutos de viaje!")
elif totalMario > totalJuan:
    print(f"Juan ha ganado con un total de {totalJuan} minutos de viaje!")
else:
    print(f"Mario y Juan empataron con un total de {totalJuan} minutos de viaje!")