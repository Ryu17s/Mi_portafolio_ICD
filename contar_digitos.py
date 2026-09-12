n = int(input())
copiaN = n
digito = 0
while copiaN > 0:
    copiaN //= 10
    digito += 1
    
if n == 0:
    print("el número ingresado es",n, "tiene 1 dígito")
elif digito == 1:
    print("el número ingresado es" ,n, "tiene" ,digito,"dígito")
else:
    print("el número ingresado es" ,n ,"tiene" ,digito,"dígitos")