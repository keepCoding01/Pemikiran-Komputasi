# ALGORITMA

# 1. INISIALISASI FUNGSI DEF OPERASIPERASIPERKALIANMATRIKS DENGAN PARAMETER DIMENSI
# 	- INISIALISASI N DENGAN NILAI DIMENSI YANG DIKURANG 1
# 	- INISIALISASI INF DENGAN NILAI INF
# 	- INISIALISASI DP DENGAN LIST KOSONG
# 	- LAKUKAN PERULANGAN SELAMA N
# 	- INISIALISASI BARIS DENGAN LIST KOSONG
# 	- LAKUKAN PERULANGAN LAGI SELAMA N
# 	- TAMBAHKAN 0 KE VARIABEL BARIS
# 	- TAMBAHKAN NILAI BARIS KE VARIABEL DP
# 	- LAKUKAN PERULANGAN PANJANG MULAI DARI 2 HINGGA N+1
# 	- LAKUKAN PERULANGAN N-PANJANG+1
# 	- SET INDEKS I DAN J DENGAN INF
# 	- LAKUKAN PERULANGAN K SELAMA I SAMPAI J
# 	- SET DI = DIMENSI KE-I, DK1 = DIMENSI K+1, DJ1 = DIMENSI J+1
# 	- SET BIAYA = INDEKS I K DARI DP DITAMBAH INDEKS K + 1 J DARI DP + HASIL KALI KETIGA NYA ( DI,DK1,DJ1 )
# 	- JIKA BIAYA < INDEKS I J PADA DP, MASUKKAN NILAINYA KE DALAM DP
# 	- KEMBALIKAN NILAINYA
# 2. INPUT NILAI
# 3. JALANKAN FUNGSI DEF OPERASIPERKALIANMARTRIKS YANG DISIMPAN KE DALAM VARIABEL JLHMINIMUM
# 4. CETAK HASILNYA

# KOMPLEKSITAS WAKTU: O(N ^ 3)
# KOMPLEKSITAS RUANG: O(N ^ 2)


def operasiPerkalianMatriks(dimensi):
    n = len(dimensi) - 1
    inf = float('inf')
    dp = []
    for _ in range(n):
        baris = []
        for _ in range(n):
            baris.append(0)
        dp.append(baris)

    for panjang in range(2, n + 1):
        for i in range(n - panjang + 1):
            j = i + panjang - 1
            dp[i][j] = inf
            for k in range(i, j):
                dI = dimensi[i]
                dK1 = dimensi[k + 1]
                dJ1 = dimensi[j + 1]

                biaya = dp[i][k] + dp[k + 1][j] + \
                    dI * dK1 * dJ1

                if biaya < dp[i][j]:
                    dp[i][j] = biaya

    return dp[0][n - 1]


jlhMatriks = int(input().strip())
masukan = input().strip().split()

dimensi = list(map(int, masukan))

jlhMinimum = operasiPerkalianMatriks(dimensi)
print(jlhMinimum)
