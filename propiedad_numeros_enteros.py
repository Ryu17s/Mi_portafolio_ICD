def sumaDivisoresPropios(num):
    if num == 1:
        return 0
    suma = 1
    for k in range(2, int(num**0.5) + 1):
        if num % k == 0:
            suma += k
            if k != num // k:
                suma += num // k
    return suma

def poblar():
    lista = []
    while True:
        linea = input().strip()
        if linea == "ONCE":
            break
        if linea.isdecimal() and int(linea) > 0 and linea not in lista:
            lista.append(linea)
    return lista

def memorables(lista):
    listaM = []
    for i in lista:
        if "11" in i:
            listaM.append(int(i))
    listaM.sort(reverse=True)
    return listaM

def deMatta(lista):
    listaDM = []
    for i in lista:
        num = int(i)
        if sumaDivisoresPropios(num) % 11 == 0:
            listaDM.append(num)
    listaDM.sort()
    return listaDM

def noMemorable(lista):
    listaNM = []
    for i in lista:
        if "11" not in i:
            listaNM.append(i)
    return listaNM

def noMatta(lista):
    listaNoMa = []
    for i in lista:
        if sumaDivisoresPropios(int(i)) % 11 != 0:
            listaNoMa.append(i)
    return listaNoMa

def noMemoYnoMatta(noMemo, noKill):
    listaFinal = []
    for i in noMemo:
        if i in noKill:
            listaFinal.append(i)
    return listaFinal

#---------------------------------------
lista = poblar()

if len(lista) == 0:
    print("LISTA DE NÚMEROS ENTEROS POSITIVOS DIFERENTES ALMACENADOS COMO CADENAS ESTÁ VACÍA")
else:
    print("LISTA DE NÚMEROS ENTEROS POSITIVOS DIFERENTES ALMACENADOS COMO CADENAS")
    print(lista)
    print("Total elementos en lista =", len(lista))

    listaM = memorables(lista)
    if len(listaM) > 0:
        print("\nLISTA DE MEMORABLES")
        for m in listaM:
            print(m)
        print("Total elementos en lista =", len(listaM))
    else:
        print("\nLISTA DE MEMORABLES ESTÁ VACÍA")

    esMatta = deMatta(lista)
    if len(esMatta) > 0:
        print("\nLISTA DE DEMATTA")
        for j in esMatta:
            print(j)
        print("Total elementos en lista =", len(esMatta))
    else:
        print("\nLISTA DE DEMATTA ESTÁ VACÍA")

    noMemo = noMemorable(lista)
    noKill = noMatta(lista)
    listaJunta = noMemoYnoMatta(noMemo, noKill)
    if len(listaJunta) > 0:
        print("\nLISTA DE NO MEMORABLES Y NO DEMATTA")
        print(listaJunta)
        print("Total elementos en lista =", len(listaJunta))
    else:
        print("\nLISTA DE NO MEMORABLES Y NO DEMATTA ESTÁ VACÍA")