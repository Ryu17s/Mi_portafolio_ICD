def procesarPuntos(listaPuntos, listaCirc):
    print("----- PROCESO DE LISTA DE PUNTOS EN FUNCIÓN -----")
    for punto in listaPuntos:
        xPunto, yPunto = punto
        print(f"Punto {punto} se encuentra al interior de")
        flag = False
    
        for circunferencia in listaCirc:
            centro, radio = circunferencia
            xCentro, yCentro = centro
            
            distancia = ((xPunto - xCentro)** 2 + (yPunto - yCentro)** 2)**0.5
            
            if distancia < radio:
                print(circunferencia)
                flag = True
                
        if flag == False:
            print("ninguna circunferencia de la lista")
    
    
    

