def poblarLista():
    lista = []
    while True:
        linea = input().upper()
        if linea == "FIN": break
        lineaSeparada = (linea.split(sep=","))
        
        for idx in range(len(lineaSeparada)):
            lineaSeparada[idx] = lineaSeparada[idx].strip()
            
        lineaSeparada[4] = int(lineaSeparada[4])
        lineaSeparada = tuple(lineaSeparada)
        lista.append(lineaSeparada)
    return lista

def mostrar(lista):
    print("REGISTROS INGRESADOS")
    print("====================")
    for elem in lista:
        print(elem)
    print("\nTOTAL ESCUCHAS =",len(lista))

def usuariosDiferente(lista):
    listaName = []
    for elem in lista:
        if elem[0] not in listaName:
            listaName.append(elem[0])
    listaName.sort()

    listaMayuscula = []
    for elem in listaName:
        listaMayuscula.append(elem.upper())
    return listaMayuscula

def resumenUsuario(lista,distinto):
    print("\nRESUMEN POR USUARIO")
    print("===================")
    
    for user in distinto:
        canciones = []
        generos = []
        segundos = 0
        for i in lista:
            usuario = i[0]
            titulo = i[1]
            artista = i[2]
            genero = i[3]
            duracion = i[4]
            
            if usuario == user:
                segundos += duracion
                canciones.append((titulo,artista))
                if genero not in generos:
                    generos.append(genero)
        canciones.sort()
        generos.sort()
        
        print(f"{user} ESCUCHÓ {len(canciones)} CANCION(ES) {segundos} [s]")
        print(f"CANCIONES-AUTOR EN ORDEN ALF. = {canciones}")
        print(f"GÉNEROS DIFERENTES EN ORDEN ALF. = {generos}\n")
    
lista = poblarLista()
distinto = usuariosDiferente(lista)

if len(lista) == 0:
    print("--- NO SE INGRESARON DATOS ---")
else:    
    mostrar(lista)   
    
    print("\nUSUARIOS DIFERENTES EN ORDEN ALFABÉTICO")
    print("=======================================")
    for k in distinto:
        print(k)
    
    print("\nTOTAL USUARIOS DIFERENTES =",len(distinto))
    
    resumenUsuario(lista,distinto)