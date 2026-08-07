num = int(input("ingrese numero: "))

cont = 0
n = 0

while True:
    n = n + (n + cont)
    cont = cont + 1
    
    if cont == num:
        break

print("Resultado = :", n)