n = int(input())
esPrimo = True

for i in range(2, n):
    if n % i == 0:
        esPrimo = False
        break

if n == 1:
    print(f"El {n} NO es primo de Sophie Germain")

elif esPrimo == True:
    esPrimo2 = True
    for i in range(2, 2 * n + 1):
        if (2 * n + 1) % i == 0:
            esPrimo2 = False
            break
            
    if esPrimo2 == True:
        print(f"El {n} SI es primo de Sophie Germain")
    else:
        print(f"El {n} NO es primo de Sophie Germain")
        
else:
    print(f"El {n} NO es primo de Sophie Germain")