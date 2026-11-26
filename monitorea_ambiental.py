def poblar():
    lista = []
    while True:
        linea = input().split()
        if "FIN_ESTACIONES" in linea: break
        for pal in linea:
            estacion = pal.upper()
            if estacion not in lista:
                lista.append(estacion)
    return lista

def mostrar(lista):
    print("LISTA DE ESTACIONES HABILITADAS =",lista)
    print("CANTIDAD DE ESTACIONES HABILITADAS :",len(lista))

def poblarTupla():
    listaTupla = []
    while True:
        linea = input().strip()
        if linea == "FIN_REGISTROS": break
    
        i = linea.split(",")
        estacion = i[0].upper()
        sensor = i[1].lower()
        codigo =i[2]
        humedad = i[3]
        tupla = (estacion,sensor,codigo,humedad)
        listaTupla.append(tupla)
    return listaTupla

def cumpleRegistro(lista,estacionesHabilitadas):
    cumple = []
    for c in lista:
        estacion = c[0]
        sensor = c[1]
        codigo = c[2]
        humedad =c[3]
        if estacion.isalpha() and estacion in estacionesHabilitadas:
            sensorValido = sensor.isalpha()
            for letra in sensor:
                if sensor.count(letra) > 1:
                    sensorValido = False
            if sensorValido:
                if codigo.isdigit() and codigo[0] != "0" and int(codigo) > 0 and codigo == codigo[::-1]:
                    if humedad.isdigit() and 0 <= int(humedad) <= 100:
                        tupla = (estacion,sensor,int(codigo),int(humedad))
                        cumple.append(tupla)
    return cumple

def promedioHumedad(cumple):
    suma = 0
    for j in cumple:
        suma += j[3]
    return round(suma / len(cumple),1)
    
def crearResumen(cumple,estacionesHabilitadas):
    resumen = []
    for estacion in estacionesHabilitadas:
        cantidad = 0
        suma = 0
        for c in cumple:
            if c[0] == estacion:
                cantidad += 1
                suma += c[3]
        if cantidad > 0:
            promedio = round(suma / cantidad,1)
            resumen.append((estacion,cantidad,promedio))
    resumen.sort()
    return resumen

def obtenerMayorPromedio(resumen):
    mayor = resumen[0][2]
    for r in resumen:
        if r[2] > mayor:
            mayor = r[2]
    estacionesMayor = []
    for r in resumen:
        if r[2] == mayor:
            estacionesMayor.append(r[0])
    return mayor, estacionesMayor

#------------------------------------
estacionesHabilitadas = poblar()
mostrar(estacionesHabilitadas)
tupla = poblarTupla()
cumple = cumpleRegistro(tupla,estacionesHabilitadas)

if len(tupla) == 0:
    print("\nNO HUBO REGISTROS DE MEDICIONES INGRESADOS - FIN DEL PROGRAMA")
else:
    print("\nREGISTROS DE MEDICIONES INGRESADOS\n")
    for i in tupla:
        print(i)
    
    print("\nCANTIDAD DE REGISTROS DE MEDICIONES INGRESADOS :",len(tupla))
    
    if len(cumple) == 0:
        print("\nNO HUBO REGISTROS DE MEDICIONES VÁLIDOS")
    else:
        print("\nLISTADO DE REGISTROS DE MEDICIONES VÁLIDOS\n")
        for i in cumple:
            print(i)
        print(f"\nTOTAL REGISTROS DE MEDICIONES VÁLIDOS : {len(cumple)}\n")
        
    porcentajeValido = (len(cumple) * 100) / len(tupla) 
    print(f"PORCENTAJE REGISTROS DE MEDICIONES VÁLIDOS {round(porcentajeValido,1)}%")
    porcentajeNoValido = (len(tupla) - len(cumple)) * 100 / len(tupla)
    print(f"PORCENTAJE REGISTROS DE MEDICIONES NO VÁLIDOS {round(porcentajeNoValido,1)}%")
    
    if len(cumple) > 0:
        promedioGeneral = promedioHumedad(cumple)
        print("PROMEDIO DE HUMEDAD REGISTROS DE MEDICIONES VÁLIDOS :", promedioGeneral)
        listaResumen = crearResumen(cumple, estacionesHabilitadas)
        print("LISTA RESUMEN =", listaResumen)
        mayorPromedio, estacionesMayor = obtenerMayorPromedio(listaResumen)
        print("MAYOR PROMEDIO DE HUMEDAD EN LISTA RESUMEN :", mayorPromedio)
        print("LISTA DE ESTACIONES CON MAYOR PROMEDIO DE HUMEDAD :", estacionesMayor)
    
    