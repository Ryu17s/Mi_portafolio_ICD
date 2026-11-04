def poblar():
    lista = []
    while True:
        pala = input()
        if pala == "FIN": break
        
        lista.append(pala)
    return lista

def esOrden(pal):
    palabra = pal.lower()
    ordenada = "".join(sorted(palabra))
    if palabra == ordenada:
        return True
    return False
    
lista = poblar()

if len(lista) == 0:
    print("No hubo palabras para analizar")
else:
    for i in lista:
        if esOrden(i):
            print(f"{i} SI es palabra con letras ordenadas")
        else:
            if not esOrden(i):
                print(f"{i} NO es palabra con letras ordenadas")