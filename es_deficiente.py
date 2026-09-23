def es_deficiente(numero):
    divisores = 0
    for i in range(1,numero):
        if numero % i == 0:
            divisores += i
        
    if divisores >= numero:
        return False
    return True