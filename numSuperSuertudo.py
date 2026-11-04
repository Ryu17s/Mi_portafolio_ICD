def poblar():
    lista = []
    while True:
        n = input()
        if n == "FIN": return lista
        sep = n.split()
        for dato in sep:
            if dato == "FIN":
                return lista
            lista.append(dato)
    return lista
    
def esSuertudo(num,requerido):
    cantSiete = num.count("7")
    totalDigito = len(num)
    if cantSiete >= requerido:
        return True
    elif cantSiete == totalDigito and totalDigito > 0:
        return True
    return False

def listaSuertudo(lista,requerido):
    listaS = []
    for numero in lista:
        if esSuertudo(numero,requerido):
            listaS.append(numero)
    return listaS

requerido = int(input())

lista = poblar()
listaS = listaSuertudo(lista,requerido)

print("Cantidad (mínimo) de 7´s requeridos para considerar a un número como supersuestudo es:",requerido)
print("\nlistado de datos =",lista)
print("\nlistado de SuperSuertudos =",listaS)
print(f"\nRESUMEN : Total de SuperSuertudos / Total de valores leídos = {len(listaS)} / {len(lista)}")