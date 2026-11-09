def poblar():
    lista = []
    while True:
        voto = input()
        if voto == "FIN":break
        lista.append(voto)
    return lista

def conteoVoto(lista):
    listaConteo = []
    for i in lista:
        if i == "APRUEBO":
            listaConteo.append(1)
        elif i == "RECHAZO":
            listaConteo.append(0)
    return listaConteo

def comision(lista,conteo,si,no):
    totalVoto = len(lista)
    dosTercio = (totalVoto * 2) / 3 
    if si >= dosTercio:
        print(f"La norma es aprobada con {si} de {len(lista)} votos.")
        if si == len(lista):
            print("LA APROBACIÓN FUE UNÁNIME!.")
    elif si > no:
        print("La norma regresa a la comisión de origen para ser reformulada.")
    else:
        print("La norma es rechazada definitivamente.")
        if no == len(lista):
            print("EL RECHAZO FUE UNÁNIME!.")
    
#---------------------------------------------

lista = poblar()
conteo = conteoVoto(lista)

print(f"En total votaron {len(lista)} convencionales en el pleno.")
print(f"La lista de votos fue = {conteo}.")

si = conteo.count(1)
no = conteo.count(0)

print(f"\nTotal de votos APRUEBO = {si}.")
print(f"Total de votos RECHAZO = {no}.\n")

comision(lista,conteo,si,no)