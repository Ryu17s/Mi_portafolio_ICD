def poblar():
    personas = 0
    lista = []
    while len(lista) < 6:
        numero = int(input())
        personas += 1
        if numero >= 1 and numero <= 41 and numero not in lista:
            lista.append(numero)
            print(f"SE AGREGÓ UN NÚMERO VÁLIDO! --> LISTA PARCIAL {lista}.")
    print(f"\nFELICIDADES SE COMPLETARON LOS 6 NÚMEROS --> LISTA FINAL {lista}.")
    print(f"EL TOTAL DE PERSONAS ENCUESTADAS FUE : {personas}.\n")
    
    print(f"ESTOS SON LOS NÚMEROS QUE DEBES JUGAR ORDENADOS = {sorted(lista)}.")
            
    return lista
    
lista = poblar()