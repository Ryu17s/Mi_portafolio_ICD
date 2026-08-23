episodio = int(input())
nivel = int(input())
puntuacionMinima = int(input())
obtenido = int(input())
vidas = int(input())

if obtenido < puntuacionMinima:
    print("Nivel no superado NO lograste el objetivo")
    vidas = vidas -1
    if vidas == 0:
        print("No te quedan más vidas.")  
    elif vidas == 1:
        print("Te queda 1 vida.")         
    else:
        print(f"Te quedan {vidas} vidas.") 
else:
    print("Genial nivel superado !")
    
    estrellas = obtenido / puntuacionMinima
    
    if estrellas >= 1 and estrellas < 2:
        print("Obtuviste 1 estrella.")
    elif estrellas >= 2 and estrellas < 3:
        print("Obtuviste 2 estrellas.")
    else:
        print("Obtuviste 3 estrellas.")
    
    if nivel == 15:
        print(f"Completaste el episodio {episodio}")
    else:
        print(f"Pasaste al nivel {nivel + 1} del episodio {episodio}")