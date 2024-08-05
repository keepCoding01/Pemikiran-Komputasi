def proses(kata):

    n = len(kata)
    dt = []
    for i in range(n):
        baris = [0 for j in range(n)]
        dt.append(baris)

    for i in range(n):
        dt[i][i] = 1

    for all in range(2, n + 1):
        for i in range(n - all + 1):
            j = i + all - 1

            if kata[i] == kata[j] and all == 2:
                dt[i][j] = 2
            elif kata[i] == kata[j]:
                dt[i][j] = dt[i + 1][j - 1] + 2
            else:
                if dt[i][j - 1] > dt[i + 1][j]:
                    dt[i][j] = dt[i][j - 1]
                else:
                    dt[i][j] = dt[i + 1][j]

    return dt[0][n - 1]


jumlahKasus = int(input())

penampung = []
for i in range(jumlahKasus):
    kata = input()
    penampung.append(kata)

penampungPalindromTerpanjang = []
for kata in penampung:
    panjangPalindromTerpanjang = proses(kata)
    penampungPalindromTerpanjang.append(panjangPalindromTerpanjang)

for i in range(jumlahKasus):
    print(penampungPalindromTerpanjang[i])
