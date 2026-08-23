while True:
    cant = int(input())
    if 1 <= cant <= 50:
        break

print("TOTAL JUGADORES A PROCESAR :", cant)
print()

suma_puntos = 0
bono15 = 0
bono10 = 0
bono5 = 0
bono0 = 0

for i in range(1, cant + 1):
    rut = input()
    partidas = int(input())
    ganadas = int(input())
    empatadas = int(input())

    perdidas = partidas - ganadas - empatadas

    pct_ganadas = (ganadas / partidas) * 100
    pct_empatadas = (empatadas / partidas) * 100
    pct_perdidas = (perdidas / partidas) * 100

    puntaje_base = (ganadas * 2) + (empatadas * 1)

    if pct_ganadas >= 85.0:
        bono = 15
        bono15 += 1
    elif pct_ganadas >= 70.0:
        bono = 10
        bono10 += 1
    elif pct_ganadas >= 60.0:
        bono = 5
        bono5 += 1
    else:
        bono = 0
        bono0 += 1

    puntaje_final = puntaje_base + bono
    suma_puntos += puntaje_final

    print(f"JUGADOR {i}      RUT = {rut}")
    print(f"PARTIDAS JUGADAS = {partidas}")
    print(f"GANADAS   = {ganadas} --> PORCENTAJE GANADAS = {round(pct_ganadas, 1):.1f}%")
    print(f"EMPATADAS = {empatadas} --> PORCENTAJE EMPATADAS = {round(pct_empatadas, 1):.1f}%")
    print(f"PERDIDAS  = {perdidas} --> PORCENTAJE PERDIDAS = {round(pct_perdidas, 1):.1f}%")
    print(f"PUNTAJE FINAL = {puntaje_final}")
    print()

promedio_puntos = round(suma_puntos / cant, 2)

print(f"PROMEDIO PUNTAJE DE LO(S) {cant} JUGADOR(ES) = {promedio_puntos}")
print(f"TOTAL JUGADOR(ES) QUE OBTUVO BONO ADICIONAL DE 15 PUNTOS  = {bono15}")
print(f"TOTAL JUGADOR(ES) QUE OBTUVO BONO ADICIONAL DE 10 PUNTOS  = {bono10}")
print(f"TOTAL JUGADOR(ES) QUE OBTUVO BONO ADICIONAL DE 5 PUNTOS  = {bono5}")
print(f"TOTAL JUGADOR(ES) QUE NO OBTUVO BONO ADICIONAL = {bono0}")