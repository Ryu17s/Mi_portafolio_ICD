def peliculasDePais(pais,lista):
    print(f"Películas de {pais}")
    encontrado = False
    for nombre, genero, anio, pe, director, duracion in lista:
        if pe.strip().lower() == pais.strip().lower():
            print(f"{nombre} - {director} - {anio}")
            encontrado = True
    if not encontrado:
        print("No hay información disponible")
    
    
def peliculasGeneroPosterioresA(genero,anioLimite,lista):
    print(f"Películas de {genero} posteriores a {anioLimite}")
    encontrado = False
    for nombre, g, anio, pais, director, duracion in lista:
        if g.strip().lower() == genero.strip().lower() and anio > anioLimite:
            print(f"{nombre} - {anio} - {pais} - {duracion}")
            encontrado = True  
            
    if not encontrado:
        print("No hay información disponible")