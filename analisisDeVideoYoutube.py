def poblar():
    lista = []
    while True:
        titulo = input()
        if titulo == "FINAL": return lista
        else:
            titulo = titulo.upper()
            horas = input()
            minutos = input()
            segundos = input()
            vistas = input()
            lista.append([titulo,horas,minutos,segundos,vistas])
            
def tupla(lista):
    listaT = []
    for i in lista:
        titulo = i[0]
        horas = int(i[1])
        minutos = int(i[2])
        segundos = int(i[3])
        vistas = int(i[4])
        tupla = (titulo,horas,minutos,segundos,vistas)
        listaT.append(tupla)
    return listaT
    
    
lista = poblar()
listaTupla = tupla(lista)

print("TOTAL VIDEOS LEÍDOS =",len(listaTupla))

print("\nDATOS VIDEOS")
print("------------")
for i in listaTupla:
    print(f"TITULO : {i[0]} - DURACION {i[1]}:{i[2]}:{i[3]} - VISTAS : {i[4]}")

listaTiempo = []
for i in listaTupla:
    listaTiempo.append(i[1]*3600 + i[2] * 60 +i[3])
sumaTiempo = sum(listaTiempo)
    
horaTotal = sumaTiempo // 3600
minutosTotales = (sumaTiempo % 3600) // 60
segundosTotales  = (sumaTiempo % 3600) % 60
print(f"\nTIEMPO TOTAL DE TODOS LOS VIDEOS {horaTotal}:{minutosTotales}:{segundosTotales}")

listaVistas = []
for i in listaTupla:
    listaVistas.append(i[4])
promVistas = round(sum(listaVistas) / len(listaVistas), 1)
print("\nPROMEDIO DE VISTAS DE TODOS LOS VIDEOS =",promVistas)

segundos = min(listaTiempo)
print("\nMENOR DURACIÓN EN SEGUNDOS =",segundos)

print("\nTÍTULO(S) VIDEO(S) + VISTAS CON MENOR DURACIÓN EN SEGUNDOS")
print("----------------------------------------------------------")
for i in listaTupla:
    if (i[1]*3600 + i[2]*60 + i[3]) == segundos:
        print(f"* {i[0]} - {i[4]} VISTAS")

listaMasMil = []
for i in listaTupla:
    if i[4] > 1000:
        listaMasMil.append(i[0])

if len(listaMasMil) > 0:
    listaMasMil.sort()
    print("\nLISTA DE VIDEOS CON MÁS DE 1000 VISTAS ORDENADOS ALFABÉTICAMENTE")
    print("----------------------------------------------------------------")
    for i in listaMasMil:
        print(i)
else:
    print("\nNO HAY VIDEOS CON MÁS DE 1000 VISUALIZACIONES")
