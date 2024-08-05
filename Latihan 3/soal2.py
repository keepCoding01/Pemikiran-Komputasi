# ALGORITMA
# 1. MULAI
# 2. INPUT ANGKA YANG DICARI
# 3. JIKA ANGKA SAMA DENGAN 0, MAKA CETAK "Angka 0 ada di urutan ke-1"
# 4. JIKA ANGKA SAMA DENGAN 1, MAKA CETAK "Angka 1 ada di urutan ke-2"
# 5. INISIALISASI DUA VARIABEL YAITU :
#       X UNTUK MENYIMPAN ANGKA SEBELUMNYA
#       Y UNTUK MENYIMPAN ANGKA SAAT INI
# 6. INISIALISASI NILAI i UNTUK MENYIMPAN URUTAN DENGAN ANGKA 2
# 7. LAKUKAN PERULANGAN :
#       CEK APAKAH Y SAMA DENGAN N, JIKA YA MAKA CETAK ANGKANYA
#       JIKA TIDAK DITEMUKAN, MAKA CETAK PESAN 0 ALIAS TIDAK DITEMUKAN
# 8. SELESAI

# KOMPLEKSITAS WAKTU = O(n)
# KOMPLEKSITAS RUANG = O(1)

n = int(input("Masukkan angka : "))

if n == 0:
    print("Angka 0 ada di urutan ke-1")
elif n == 1:
    print("Angka 1 ada di urutan ke-2")
else:
    x = 0
    y = 1
    i = 2
    while y <= n:
        if y == n:
            print(f"Angka {n} ada di urutan ke-{i}")
            break
        x, y = y, x + y
        i += 1
    else:
        print(f"0 alias Angka {n} tidak ditemukan dalam deret Fibonacci")
