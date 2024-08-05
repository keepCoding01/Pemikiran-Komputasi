# ALGORITMA
# 1. MULAI
# 2. BUAT FUNGSI ABPA DAN MASUKKAN P SEBAGAI PARAMETERNYA
# 3. INISIALISASI K SEBAGAI ARRAY UNTUK MENAMPUNG NILAI P
# 4. INISIALISASI HASIL SEBAGAI ARRAY KOSONG
# 5. LAKUKAN PERULANGAN i UNTUK MENGHITUNG NILAI P :
#       LAKUKAN PERULANGAN j MELALUI INDEKS i + 1 SAMPAI K
#       TAMBAHKAN NILAI ABSOLUT P[i] - P[j] KE ARRAY HASIL
# 6. KEMBALIKAN NILAI HASIL
# 7. BUAT FUNGSI UPDATE ARRAY DENGAN PARAMETER A, X, Y
# 8. GANTI NILAI PADA INDEKS X - 1 DENGAN Y
# 9. BUAT FUNGSI DEF PROSES QUERY DENGAN PARAMETER A
# 10. HITUNG NILAI MAKSIMUM DAN KEMBALIKAN NILAINYA
# 11. INPUT NILAI N DAN Q
# 12. INPUT NILAI A
# 13. LAKUKAN PERULANGAN i SEBANYAK Q KALI
#       JIKA NILAI QUERY SAMA DENGAN 1, MAKA AMBIL NILAI X DAN Y SERTA PANGGIL FUNGSI UPDATE ARRAY
#       JIKA NILAI QUERY SAMA DENGAN 2, MAKA PANGGIL FUNGSI PROSES QUERY UNTUK MENGHITUNG HASIL
# 14. CETAK HASIL
# 15. SELESAI


# KOMPLEKSITAS = O(Q * K^2)
# KOMPLEKSITAS RUANG = O(Q * K)


def ABPA(P):
    K = len(P)
    hasil = []
    for i in range(K):
        for j in range(i + 1, K):
            hasil.append(abs(P[i] - P[j]))
    return hasil


def updateArray(A, X, Y):
    A[X - 1] = Y


def prosesQuery(A):
    return max(ABPA(ABPA(A)))


N, Q = map(int, input(
    "Masukkan panjang array A spasi berapa jumlah buah query = ").split())
A = list(map(int, input("Masukkan nilai untuk array A = ").split()))

for i in range(Q):
    query, *args = map(int, input(f"Nilai query ke-{i + 1} = ").split())
    if query == 1:
        X, Y = args
        updateArray(A, X, Y)
    elif query == 2:
        hasil = prosesQuery(A)
        print("Nilai query sekarang = ", hasil)
