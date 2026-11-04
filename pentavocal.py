def crearLista():
    lista = []
    while True:
        palabra = input()
        if palabra =="FIN": break
        lista.append(palabra)
    return lista
    
def pentavocal(palabra):
    cont = 0
    minuscula = palabra.lower()
    for letra in minuscula:
        if letra in "aeiou":
            if minuscula.count(letra) > 1:
                return False
        else:
            cont +=1
    
    if cont == len(palabra) - 5:
        return True
    else: 
        return False

lista = crearLista()

if len(lista) == 0:
    print("No hubo palabras a analizar")
else:
    for i in lista:
        if pentavocal(i):
            print(f"{i} SI es pentavocálica")
        else:
            print(f"{i} NO es pentavocálica")