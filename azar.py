def procesarCartones(numGanador, listaCarton):
    print("***  SALIDA FUNCION PROCESAR CARTONES  ***")
    i = 1 
    for carton in listaCarton:
        cumple = 0
        for numero in carton:
            if numero in numGanador:
                cumple += 1
        mensaje = (f"Cartón {i} : {carton} tiene {cumple} aciertos")
        if cumple == len(numGanador):
            mensaje += (" - Cartón Ganador!")
        print(mensaje)
        i += 1