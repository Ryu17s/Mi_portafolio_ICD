def poblar():
    lista = []
    while True:
        linea = input()
        if linea == "FIN": 
            return lista
        lista.append(linea)

def repetidas(frase):
    for signo in [".", ",", ";", ":"]:
        frase = frase.replace(signo, "")
    
    palabras = frase.lower().split()
    
    repe = []
    for pal in palabras:
        if palabras.count(pal) > 1 and pal not in repe:
            repe.append(pal)
            
    repe.sort()
    return repe

lista = poblar()

if len(lista) == 0:
    print("No hubo frases para analizar")
else:
    for x, frase in enumerate(lista, 1):
        listaRepe = repetidas(frase)
        print(f"Frase {x} - palabras repetidas : {listaRepe}")
