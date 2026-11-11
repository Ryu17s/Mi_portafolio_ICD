def cantPartidas():
    while True:
        partidas = int(input())
        if partidas > 0:
            return partidas 
    
def poblar():
    n = cantPartidas()
    lista = []
    while len(lista) < n:
        player = input()
        personaje = input()
        mundo = int(input())
        nivel = int(input())
        monedas = int(input())
        
        tupla = (player, personaje, mundo, nivel, monedas)
        lista.append(tupla)
    return lista

def money(lista):
    listaMoney = []
    for partida in lista:  
        listaMoney.append(partida[4]) 
    masMoneda = max(listaMoney)
    return masMoneda
    
def mejorJugador(lista, masMoneda):
    bestJugador = []
    for partida in lista:
        if partida[4] == masMoneda:
            bestJugador.append(partida[0])
    return bestJugador
    
def masUsado(lista):
    listaPersonajes = []
    for partida in lista:
        listaPersonajes.append(partida[1])
        
    maxRepeticiones = 0
    for personaje in listaPersonajes:
        if listaPersonajes.count(personaje) > maxRepeticiones:
            maxRepeticiones = listaPersonajes.count(personaje)
            
    personajesGanadores = []
    for personaje in listaPersonajes:
        if listaPersonajes.count(personaje) == maxRepeticiones:
            if personaje not in personajesGanadores:
                personajesGanadores.append(personaje)
            
    return personajesGanadores

def masJugado(lista):
    listaMundos = []
    for partida in lista:
        listaMundos.append(partida[2])
        
    maxRepeticiones = 0
    for mundo in listaMundos:
        if listaMundos.count(mundo) > maxRepeticiones:
            maxRepeticiones = listaMundos.count(mundo)
            
    mundosGanadores = []
    for mundo in listaMundos:
        if listaMundos.count(mundo) == maxRepeticiones:
            if mundo not in mundosGanadores:
                mundosGanadores.append(mundo)
            
    mundosGanadores.sort()
    return mundosGanadores

lista = poblar()
masMoneda = money(lista)

print("LISTA DE PARTIDAS")
print("-----------------")
for partida in lista:
    print(partida)

print("\nLA MAYOR CANTIDAD DE MONEDAS FUE", masMoneda)
print("JUGADOR(ES) QUE RECOLECTARON MAYOR CANTIDAD DE MONEDAS")
print("------------------------------------------------------")
ganadores = mejorJugador(lista, masMoneda)
for i in ganadores:
    print(i)

print(f"\nPERSONAJE(S) MÁS USADO(S) = {masUsado(lista)}")
print(f"\nMUNDO(S) MÁS JUGADO(S) = {masJugado(lista)}")
