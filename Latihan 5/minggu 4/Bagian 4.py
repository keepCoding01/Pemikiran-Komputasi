angka = list(map(int,input().split()))
jumlah = []
for i in range (10):
    jumlah.append(0)

for i in range(len(angka)):
    jumlah[angka[i]] += 1

maxi = -1

for i in range(len(jumlah)):
    if (jumlah[i]>maxi):
        maxi = jumlah[i]
        modus = i

print("Modus : ", modus)
