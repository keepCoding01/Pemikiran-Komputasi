# kompleksitas : Big O -> O(N^2)
N = list(map(int, input().split()))
K = N[1]
C = []
temp = list(map(int, input().split()))
for i in range(N[0]):
    C.append(temp[i])
for i in range(len(C)):
    for j in range(i, len(C)):
        if C[i] > C[j]:
            x = C[i]
            C[i] = C[j]
            C[j] = x

Stock = C[::-1]
Pembelian = []
x = -1
for i in range(N[0]):
    if i % K == 0:
        x += 1
    Pembelian.append(x)

Hasil = []
for i in range(N[0]):
    temp = (Pembelian[i]+1 * Stock[i])
    Hasil.append(temp)

Min = 0
for i in range(len(Hasil)):
    Min += Hasil[i]
print(Min)
