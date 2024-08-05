# ALGORITMA

# 1. INISIALISASI FUNGSI DEF HITUNGJLHOPERASI DENGAN PARAMETER N, STRINGA, STRINGB
# 	- INISIALISASI VARIABEL A DENGAN LIST STRINGA
# 	- INISIALISASI VARIABEL B DENGAN LIST STRINGB
# 	- INISIALISASI VARIABEL JLHOPERASI DENGAN NILAI 0
# 	- INISIALISASI VARIABEL INDEKS DENGAN NILAI 0
# 	- LAKUKAN PERULANGAN WHILE SELAMA INDEKS < N
# 	- JIKA INDEKS A > INDEKS B, MULAI = INDEKS TERSEBUT
# 	- LAKUKAN PERULANGAN KEMBALI SELAMA INDEKS < N DAN INDEKS A > INDEKS B, KEMUDIAN TAMBAHKAN 1 DI TIAP-TIAP VARIABEL INDEKS
# 	- VARIABEL AKHIR = INDEKS - 1
# 	- VARIABEL PANJANG = AKHIR - MULAI + 1
# 	- INDEKS A, INDEKS B = INDEKS B
# 	- TAMBAHKAN 1 TIAP JLHOPERASI, JIKA TIDAK TAMBAHKAN 1 TIAP INDEKS
# 	- KEMBALIKAN NILAINYA
# 2. INPUT NILAI N, STRINGA, STRINGB DAN CETAK HASILNYA DENGAN MENJALANKAN FUNGSI HITUNGJLHOPERASI

# KOMPLEKSITAS WAKTU = O(N^2)
# KOMPLEKSITAS RUANG = O(N)
def hitungJlhOperasi(N, stringA, stringB):
    A = list(stringA)
    B = list(stringB)
    jlhOperasi = 0
    indeks = 0

    while indeks < N:
        if A[indeks] > B[indeks]:
            mulai = indeks
            while indeks < N and A[indeks] > B[indeks]:
                indeks += 1
            akhir = indeks - 1
            panjang = akhir - mulai + 1
            A[mulai:mulai+panjang], B[mulai:mulai +
                                      panjang] = B[mulai:mulai+panjang], A[mulai:mulai+panjang]
            jlhOperasi += 1
        else:
            indeks += 1

    return jlhOperasi


N = int(input().strip())
stringA = input().strip()
stringB = input().strip()

print(hitungJlhOperasi(N, stringA, stringB))
