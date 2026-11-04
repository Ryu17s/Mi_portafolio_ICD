def poblar():
    lista = []
    while True:
        linea = input().split()
        for dato in linea:
            if dato == "FIN": return lista
            if dato.isdigit():
                dato = int(dato)
                if dato > 0 and dato not in lista:
                 lista.append(dato)
    return lista


def mayorDato(dato):
    datoMenor = ''.join(sorted(str(dato)))
    datoMayor = ''.join(sorted(str(dato), reverse=True))
    
    return datoMenor, datoMayor
    
def divisible9(dato):
    if dato % 9 == 0:
        return True
    return False

#-----------------------------------------------------

lista = sorted(poblar())
if len(lista) > 0:
    print("LISTA DE NÚMEROS ORDENADOS DE MENOR A MAYOR =",lista)
    print("TOTAL DE NÚMEROS INGRESADOS =",len(lista))
    print("\n------------ PROCESAMIENTO DE NÚMEROS EN LISTA ------------\n")

    for dato in lista:
        datoMenor, datoMayor = mayorDato(dato)
        resta = int(datoMayor) - int(datoMenor)
        
        if divisible9(resta):
            o = resta // 9
            print("NÚMERO ORIGINAL =",dato)
            print("MAYOR NÚMERO CON LOS MISMOS DÍGITOS :",datoMayor)
            print("MENOR NÚMERO CON LOS MISMOS DÍGITOS :",datoMenor)
            print(f"{datoMayor} - {datoMenor} = {resta} = {o} x 9\n")
else:
    print("NO SE INGRESARON NÚMEROS ENTEROS POSITIVOS MAYORES A 0")