def validar():
    while True:
        n = int(input())
        if n >= 1: 
            break
    return n

def contar_digitos(n):
    contador = 0
    while n > 0:
        contador += 1
        n //= 10
    return contador

def kaprekar(numero):
    cuadrado = numero ** 2
    n_digitos = contar_digitos(numero)
    divisor = 10 ** n_digitos
    
    izq = cuadrado // divisor
    der = cuadrado % divisor
    
    return (izq + der) == numero

numero = validar()

if kaprekar(numero):
    print(numero, "ES UN NÚMERO DE KAPREKAR")
else:
    print(numero, "NO ES UN NÚMERO DE KAPREKAR")