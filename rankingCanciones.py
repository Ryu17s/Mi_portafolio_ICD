def procesar_ranking(lista_canciones):
    ranking = sorted(lista_canciones, reverse=True)
    
    print("Número de Registro - Total de Reproducciones")
    print("============================================")
    for reproducciones, codigo in ranking:
        print("         " + str(codigo) + "                  " + str(reproducciones))    