acak = list(map(int, input().split()))
bilanganPrima = 0

for angka in acak:
    if angka < 2:
        continue
    prima = True
    for i in range(2, int(angka**0.5)+1):
        if angka % i == 0:
            prima = False
            break
    if prima:
        bilanganPrima += 1
print(bilanganPrima)
