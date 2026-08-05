def leerLista():
    n = int(input(":"))
    lista = []
    for i in range(n):
        num = int(input("z:"))
        lista.append(num)
    return lista

def alternada(lista):
    for i in range(len(lista) - 1):
        if lista[i] % 2 == lista[i+1] % 2:
            return False
    return True

copiaLista = leerLista()

print(f"Lista = {copiaLista}")

if alternada(copiaLista):
    print("La lista SI es alternada par-impar ")
else:
    print("La lista NO es alternada par-impar ")