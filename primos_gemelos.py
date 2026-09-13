p = int(input())
q = int(input())

contP = 0
contQ = 0
for i in range(1,p+1):
    if p % i == 0:
        contP += 1

for i in range(1,q+1):
    if q % i == 0:
        contQ += 1

primoP = contP == 2 and p > 1
primoQ = contQ == 2 and q > 1

if p < q:
    if primoP and primoQ and q - p == 2:
            print(f"Los números ({p},{q}) SI son primos gemelos")
    else:
        print(f"Los números ({p},{q}) NO son primos gemelos")
else:
    if primoP and primoQ and p - q == 2:
            print(f"Los números ({q},{p}) SI son primos gemelos")
    else:
        print(f"Los números ({q},{p}) NO son primos gemelos")
    


