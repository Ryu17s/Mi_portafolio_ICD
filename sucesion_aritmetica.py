while True:
    n = int(input())
    if 1 <= n <= 100: break

total = 1

for i in range(1,n+1):
    print(total, end= " ")
    total += 3
    
    if n == 0:
        print("1")
    