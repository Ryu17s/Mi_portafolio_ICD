def transformar(original):
    largo = len(original)

    for i in range(largo):
        if i % 2 == 0:
            original[i] += 1
        else: 
            original[i] -= 1

def poblar():
    lista = []
    while True:
        edad = int(input())
        if edad < 0: break
        lista.append(edad)
    return lista
    

    
original = poblar()
print("Lista Original =",original)
transformar(original)
print("Lista Nueva =",original)