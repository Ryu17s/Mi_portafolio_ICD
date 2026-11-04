cant = int(input())

for i in range(cant):
    p1 = input()
    p2 = input()
    
    cumple = True
    if len(p1) != len(p2):
        cumple = False
    else:
        for letra in p1.lower():
            if letra not in p2.lower():
                cumple = False
                break
    if cumple:
        print(f"{p1} & {p2} SI son anagramas\n")
    else:
        print(f"{p1} & {p2} NO son anagramas\n")