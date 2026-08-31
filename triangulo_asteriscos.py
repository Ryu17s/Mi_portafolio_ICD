while True:
    altura = int(input())
    if altura > 0 and altura < 21: break

for i in range(1,altura +1):
    print("*" * i)