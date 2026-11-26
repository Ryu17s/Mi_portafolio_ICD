def poblar():
    lista = []
    while True:
        linea = input().split()
        for dato in linea:
            if dato == "FIN":return lista
            if dato.isdigit():
                numero = int(dato)
                if numero > 0 and numero not in lista:
                    lista.append(numero)
    return lista


def mostrar(lista):
    print("LISTA NÚMEROS ENTEROS MAYORES A CERO DIFERENTES INGRESADOS =",lista)
    print("TOTAL DE NÚMEROS EN LA LISTA =",len(lista))


def procesar(numero):
    texto = str(numero)
    n = len(texto)
    
    if n > 9: return False, n
    
    for i in range(1, n + 1):
        digito_buscado = str(i)
        if digito_buscado not in texto:
            return False, n
            
    return True, n


def cumple(lista):
    lista_tuplas = []
    for numero in lista:
        es_pan, n = procesar(numero)
        if es_pan:
            print(f"NÚMERO {numero} TIENE {n} DÍGITO(S) --> ES {n}-PANDIGITAL.")
            lista_tuplas.append((numero, n))
        else:
            print(f"NÚMERO {numero} TIENE {n} DÍGITO(S) --> NO ES {n}-PANDIGITAL.")
    return lista_tuplas


def reporte(lista_tuplas):
    print("LISTA DE N-PANDIGITALES ORIGINAL =",lista_tuplas)
    print(f"LA LISTA TIENE {len(lista_tuplas)} TUPLA(S).")
    print("\n========================================================================")
    print("REPORTE FINAL")
    print("========================================================================\n")
    
    digitos = []
    for tupla in lista_tuplas:
        if tupla[1] not in digitos:
            digitos.append(tupla[1])
    digitos.sort()
    
    print("LISTA DE CANTIDAD DE DÍGITOS DIFERENTES PROCESADOS =",digitos)
    
    for d in digitos:
        ordenados = []
        for tupla in lista_tuplas:
            if tupla[1] == d:
                ordenados.append(tupla[0])
        ordenados.sort(reverse=True)
        print(f"NÚMEROS {d}-DIGITALES =",ordenados)


lista = poblar()

if len(lista) == 0:
    print("NO SE INGRESARON NÚMEROS ENTEROS POSITIVOS Y MAYORES A 0.")
else:
    mostrar(lista)
    print("\n------------ PROCESAMIENTO DE NÚMEROS EN LISTA ------------\n")
    lista_tuplas = cumple(lista)
    print("\n------------ FIN PROCESAMIENTO DE NÚMEROS EN LISTA ------------\n")
    
    if len(lista_tuplas) == 0:
        print("NO SE ENCONTRARON NÚMEROS N-PANDIGITALES.")
    else:
        reporte(lista_tuplas)