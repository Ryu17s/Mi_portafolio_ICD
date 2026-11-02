def obtenerNumeroRut(rut):
    return int(rut.split("-")[0])

def poblarLista(cantPaciente):
    lista = []
    for i in range(cantPaciente):
        rut = input().strip()
        nombre = input().strip()
        edad = int(input().strip())
        resultado = input().strip()
        
        tupla = (rut, nombre, edad, resultado)
        lista.append(tupla)
    return lista

def mostrarLista(lista, cantPaciente):
    print("LISTADO DE PERSONAS QUE SE REALIZARON PCR")
    print("=========================================")
    for i in lista:
        print(f"{i[0]} {i[1]} {i[2]} {i[3]}")

def contarPaciente(lista, cantPaciente):
    contP = 0
    contN = 0
    for i in lista:
        if i[3] == "POSITIVO":
            contP += 1
        else:
            contN += 1
    return contP, contN

def ordenarRuts(listaRuts):
    for i in range(len(listaRuts)):
        for j in range(len(listaRuts) - 1):
            if obtenerNumeroRut(listaRuts[j]) > obtenerNumeroRut(listaRuts[j + 1]):
                aux = listaRuts[j]
                listaRuts[j] = listaRuts[j + 1]
                listaRuts[j + 1] = aux
    return listaRuts

def positivos(lista, cantPaciente):
    listaP = []
    for i in lista:
        if i[3] == "POSITIVO":
            listaP.append(i)

    if len(listaP) > 0:
        print("Listado Ordenado Por Rut de Personas con PCR POSITIVO")
        ruts = []
        for persona in listaP:
            ruts.append(persona[0])
        
        rutsOrdenados = ordenarRuts(ruts)
        for rut in rutsOrdenados:
            print(rut)

        print()

        mayor = 0
        menor = 0
        for i in listaP:
            if i[2] >= 18:
                mayor += 1
            else:
                menor += 1

        pctMayor = round((mayor * 100 / len(listaP)), 1)
        pctMenor = round((menor * 100 / len(listaP)), 1)
        print(f"El {pctMayor:.1f} % de personas con PCR POSITIVO eran MAYORES DE EDAD.")
        print(f"El {pctMenor:.1f} % de personas con PCR POSITIVO eran MENORES DE EDAD.")
    else:
        print("NO hay personas con PCR POSITIVO.")

cantPaciente = int(input().strip())
lista = poblarLista(cantPaciente)
mostrarLista(lista, cantPaciente)
resultados = contarPaciente(lista, cantPaciente)
print()

print("REPORTE MINSAL")
print("==============\n")

pctPos = round(resultados[0] * 100 / cantPaciente, 1)
pctNeg = round(resultados[1] * 100 / cantPaciente, 1)
print(f"El {pctPos:.1f} % de las personas procesadas tiene PCR POSITIVO")
print(f"El {pctNeg:.1f} % de las personas procesadas tiene PCR NEGATIVO\n")
pcrPos = positivos(lista, cantPaciente)