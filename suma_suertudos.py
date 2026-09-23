def esSuertudo(X):
    while X:
        digito = X % 10
        X //= 10
        if digito == 7:
            return True
    return False
    
def sumarSuertudos(A,B):
    suma = 0
    for i in range(A,B+1):
        if esSuertudo(i):
            suma += i
    return suma