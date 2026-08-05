def poblar(total):
    listaD = []
    for i in range(total):
        print(f"\n--- Persona {i + 1} ---")
        rut = input("Ingrese RUT: ")
        nombre = input("Ingrese Nombre: ")
        edad = int(input("Ingrese Edad: "))
        resultado = input("Ingrese Resultado (POSITIVO/NEGATIVO): ")
        tuplaD = (rut, nombre, edad, resultado)
        listaD.append(tuplaD)
    return listaD

def mostrar_lista(lista):
    print("LISTADO DE PERSONAS QUE SE REALIZARON PCR")
    print("=========================================")
    for p in lista:
        print(f"{p[0]} {p[1]} {p[2]} {p[3]}")

def generar_reporte(lista):
    print("\nREPORTE MINSAL")
    print("==============")
    print()
    total = len(lista)
    if total == 0:
        return
    positivos = 0
    negativos = 0
    ruts_positivos = []
    mayores_positivos = 0
    menores_positivos = 0
    for p in lista:
        if p[3] == "POSITIVO":
            positivos += 1
            ruts_positivos.append(p[0])
            if p[2] >= 18:
                mayores_positivos += 1
            else:
                menores_positivos += 1
        elif p[3] == "NEGATIVO":
            negativos += 1
    porcentaje_pos = (positivos / total) * 100
    porcentaje_neg = (negativos / total) * 100
    print(f"El {round(porcentaje_pos, 1)} % de las personas procesadas tiene PCR POSITIVO")
    print(f"El {round(porcentaje_neg, 1)} % de las personas procesadas tiene PCR NEGATIVO")
    print()
    if positivos == 0:
        print("NO hay personas con PCR POSITIVO.")
    else:
        print("Listado Ordenado Por Rut de Personas con PCR POSITIVO")
        ruts_positivos.sort()
        for r in ruts_positivos:
            print(r)
        print()
        porc_mayores = (mayores_positivos / positivos) * 100
        porc_menores = (menores_positivos / positivos) * 100
        print(f"El {round(porc_mayores, 1)} % de personas con PCR POSITIVO eran MAYORES DE EDAD.")
        print(f"El {round(porc_menores, 1)} % de personas con PCR POSITIVO eran MENORES DE EDAD.")

nPersonas = int(input("Ingrese la cantidad de personas a registrar: "))
listaTpersonas = poblar(nPersonas)
mostrar_lista(listaTpersonas)
generar_reporte(listaTpersonas)