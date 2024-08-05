def proses(koin, jumlahKoin):
    n = len(koin)
    dt = [float('inf')] * (jumlahKoin + 1)

    dt[0] = 0

    for i in koin:
        for j in range(jumlahKoin + 1):
            if i <= j:
                dt[j] = min(dt[j], dt[j - i] + 1)

    return dt[jumlahKoin]


banyakKoin = int(input("jumlah : "))
nilaiKoin = []
for i in range(banyakKoin):
    nilaiKoin.append(int(input(f"nilai koin ke-{i+1}: ")))
kembalian = int(input("kembalian : "))

minimalKembalian = proses(nilaiKoin, kembalian)

print("minimal kembalian : ", minimalKembalian)
