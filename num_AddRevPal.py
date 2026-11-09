def poblar():
    lista = []
    while True:
        linea = input()
        dato = linea.split()
        for d in dato:
            if d == "FIN":
                return lista
            if d.isdigit():
                numero = int(d)
                if numero > 9 and numero not in lista:
                    lista.append(numero)
    return lista


def mostrarListaIngresados(lista):
    print("LISTA NÚMEROS ENTEROS POSITIVOS MAYORES A 9 INGRESADOS")
    print("LISTA NÚMEROS ORDENADOS DE MENOR A MAYOR =", lista)
    total = len(lista)
    print("TOTAL DE NÚMEROS =", total)


def mostrarListaTuplas(lista):
    print("LISTA DE TUPLAS CON NÚMEROS ADD-REV-PAL")
    print("LISTA ADD-REV-PAL ORDENADA DE MAYOR A MENOR =", lista)
    total = len(lista)
    print("TOTAL DE TUPLAS =", total)


def fnEspejo(numero):
    numeroC = str(numero)
    esp = numeroC[::-1]
    numEspejo = int(esp)
    return numEspejo


def procesar(lista):
    print()
    print("----- PROCESAMIENTO DE NÚMEROS -----")
    print()

    listaNueva = []

    for num in lista:
        espejo = fnEspejo(num)
        suma = num + espejo
        espejoSuma = fnEspejo(suma)
        print("NÚMERO =", num)
        print("ESPEJO NÚMERO =", espejo)
        print("SUMA NÚMERO + ESPEJO =", suma)
        if suma == espejoSuma:
            print(suma, "ES PALÍNDROMO\n")
            tupla = (num, espejo, suma)
            listaNueva.append(tupla)
        else:
            print(suma, "NO ES PALÍNDROMO\n")
    return listaNueva


lista = poblar()

if len(lista) == 0:
    print("NO SE INGRESARON NÚMEROS ENTEROS POSITIVOS MAYORES A 9.")
else:
    lista.sort()
    mostrarListaIngresados(lista)

    addRevPal = procesar(lista)
    if addRevPal == []:
        print("NO SE ENCONTRARON NÚMEROS ADD-REV-PAL.")
    else:
        addRevPal.sort(reverse=True)
        mostrarListaTuplas(addRevPal)