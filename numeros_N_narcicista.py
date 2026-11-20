def poblar():
    lista = []
    while True:
        linea = input()
        if linea == "FIN": break
        if linea.isdigit():
            if int(linea) > 0 and linea not in lista:
                lista.append(linea)
    return lista

def listaEntero(lista):
    listaInt = []
    for elem in lista:
        listaInt.append(int(elem))
    listaInt.sort()
    return listaInt

def tuplaNarci(lista):
    listaTuplas = []
    for n in lista:
        cadena = str(n)
        cantidad = len(cadena)
        suma = 0
        for digito in cadena:
            suma += int(digito) ** cantidad
        tupla = (n, cantidad, suma)
        listaTuplas.append(tupla)
    return listaTuplas
    
def cumple(lista):
    listaCumple = []
    for i in lista:
        if i[0] == i[2]:
            listaCumple.append(i[0])
    return listaCumple
    
def totalLista(lista):
    return len(lista)
    
def mostrar(lista):
    if len(lista) == 0:
        print("LISTA INICIAL DE CADENAS VACIA")
    else:
        print("LISTA INICIAL DE CADENAS =", lista)

lista = poblar()
cantidadLista = totalLista(lista)

mostrar(lista)
if len(lista) > 0:
    print("TOTAL ELEMENTOS EN LISTA INICIAL DE CADENAS =", cantidadLista)
    numerosOrdenados = listaEntero(lista)
    print("LISTA NUMEROS EN ORDEN CRECIENTE =", numerosOrdenados)
    
    tuplas = tuplaNarci(numerosOrdenados)
    print("LISTA TUPLAS =", tuplas)
    
    narcisistas = cumple(tuplas)
    if len(narcisistas) == 0:
        print("NO SE ENCONTRARON NÚMEROS N-NARCISISTAS EN LA LISTA")
    else:
        print("LISTA DE NÚMEROS N-NARCISISTAS =", narcisistas)
        print("TOTAL ELEMENTOS EN LISTA DE NÚMEROS N-NARCISISTAS =", totalLista(narcisistas))
        print("--- GRAN NARCISISMO ---")