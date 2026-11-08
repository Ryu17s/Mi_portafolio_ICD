def poblar():
    lista = []
    while True:
        entrada = input()
        if entrada == "0 0": 
            break
    
        parte = entrada.split()
        
        if len(parte) == 2 and parte[0].isdigit() and parte[1].isdigit():
            n1 = int(parte[0])
            n2 = int(parte[1])
            
            if n1 > 9 and n2 > 9:
                tupla = (n1, n2)
                if tupla not in lista and (n2, n1) not in lista:
                    lista.append(tupla)
                    
    return lista


def mostrar_inicial(lista):
    if len(lista) == 0:
        print("NO SE INGRESARON PARES DE NÚMEROS ENTEROS MAYORES A 9")
        return False
    else:
        lista_ordenada = sorted(lista)
        print("LISTA TUPLAS INICIAL ORDENADA MENOR A MAYOR =", lista_ordenada)
        print("TOTAL DE ELEMENTOS LISTA =", len(lista_ordenada))
        print("---------------------------------------")
        return True


def filtrar_permutables(lista):
    lista_base = sorted(lista)
    permutables = []
    for n1, n2 in lista_base:
        str1 = str(n1)
        str2 = str(n2)
        if len(str1) == len(str2):
            son_permutables = True
            for digito in str1:
                if str1.count(digito) != str2.count(digito):
                    son_permutables = False
                    break
            if son_permutables:
                permutables.append((n1, n2))
    return permutables


def mostrar_permutables(lista_permutables):
    if len(lista_permutables) == 0:
        print("NO HAY PARES DE NÚMEROS PERMUTABLES EN LA LISTA INICIAL")
        return False
    else:
        print("LISTA TUPLAS NÚMEROS PERMUTABLES =", lista_permutables)
        print("TOTAL DE ELEMENTOS LISTA =", len(lista_permutables))
        print("---------------------------------------")
        return True


def filtrar_distancia_par(lista_permutables):
    lista_distancia_par = []
    for n1, n2 in lista_permutables:
        if n1 > n2:
            mayor = n1
            menor = n2
        else:
            mayor = n2
            menor = n1
        distancia = mayor - menor
        if distancia % 2 == 0:
            lista_distancia_par.append((n1, n2))
    lista_final_ordenada = sorted(lista_distancia_par, reverse=True)
    print("LISTA TUPLAS NÚMEROS PERMUTABLES CON DISTANCIA PAR ORDENADA MAYOR A MENOR =", lista_final_ordenada)
    print("TOTAL DE ELEMENTOS LISTA =", len(lista_final_ordenada))
    print("---------------------------------------")


lista_inicial = poblar()
if mostrar_inicial(lista_inicial):
    lista_permutables = filtrar_permutables(lista_inicial)
    if mostrar_permutables(lista_permutables):
        filtrar_distancia_par(lista_permutables)
