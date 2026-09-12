while True:
    n = int(input())
    if n > 0: break

copia = n
reves = 0

while copia > 0:
    digito = copia % 10
    reves = (reves * 10) + digito
    copia //= 10
    

if n == reves:
    print(n,"SI es palindromo")
else:
    print(n,"NO es palindromo")