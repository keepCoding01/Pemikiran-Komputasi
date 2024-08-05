pattern = input()
teks = input()

m = len(pattern)
n = len(teks)
cari = 0

for i in range(n-m+1):
    j = 0
    while j < m:
        if teks[i+j] != pattern[j]:
            break
        j += 1
    if j == m:
        cari = True
        break
if cari:
    print("ketemu")
else:
    print("tidak ketemu")
