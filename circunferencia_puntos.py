def procesarPuntos(puntos,circunferencia):
    print("----- PROCESO DE LISTA DE PUNTOS EN FUNCIÓN -----")
    for x,y in puntos:
        print(f"Punto ({x}, {y}) se encuentra al interior de")
        hay = False
        for circ in circunferencia:
            centro , radio = circ
            xc , yc = centro
            distancia = ((xc -x) ** 2 + (yc - y)**2) ** 0.5
            if distancia < radio:
                hay = True
                print(circ)
        if not hay:
            print("ninguna circunferencia de la lista")