def poblar():
    lista = []
    while True:
        linea = input().strip()
        if linea == "0-0": break
        dato = linea.split(",")
        
        rut = dato[0]
        titulo = dato[1].upper()
        autor = dato[2].upper()
        tematica = dato[3].upper()
        fecha = dato[4]
        
        tupla = (rut,titulo,autor,tematica,fecha)
        lista.append(tupla)
    return lista

def listaDeRut(lista):
    listaRut = []
    for i in lista:
        if i[0] not in listaRut:
            listaRut.append(i[0])
    return listaRut

def librosDiferentes(lista):
    libros = []
    for i in lista:
        distinto = (i[1],i[2])
        if distinto not in libros:
            libros.append(distinto)
    libros.sort()
    return libros

def resumenUsuario(lista,rutOrden):
    listaResumen = []
    for rut in rutOrden:
        cont = 0
        tema = []
        for i in lista:
            if i[0] == rut:
                cont += 1
                if i[3] not in tema:
                    tema.append(i[3])
        tema.sort()
        tupla = (rut,cont,tema)
        listaResumen.append(tupla)
    return listaResumen
    
def mostrar(lista):
    print("REGISTROS INGRESADOS")
    print("====================")
    for tupla in lista: 
        print(tupla)
        
lista = poblar()
rutOrden = listaDeRut(lista)
libros = librosDiferentes(lista)
resumen = resumenUsuario(lista,rutOrden)
if len(lista) == 0:
    print("--- NO SE INGRESARON DATOS ---")
else:
    mostrar(lista)
    print("\nTOTAL REGISTROS =", len(lista))
    print("\nRUT USUARIOS DIFERENTES EN ORDEN DE INGRESO =",rutOrden)
    print("TOTAL DE USUARIOS DIFERENTES =",len(rutOrden))
    print("\nTÍTULOS DE LIBROS DIFERENTES + AUTOR ORDENADOS ALFABÉTICAMENTE")
    print("=================================================================")
    for i in libros:
        print(i)
    print("\nTOTAL DE LIBROS DIFERENTES =",len(libros))
    
    print("\nRESUMEN USUARIOS - TOTAL LIBROS PEDIDOS - TEMÁTICAS")
    print("===================================================")
    for re in resumen:
        print(re)
