# ALGORITMA
# 1. MULAI
# 2. BUAT FUNGSI DEF MINIMAL SOAL DENGAN PARAMETER ANAK
# 3. LAKUKAN PERULANGAN n SEPANJANG ANAK
# 4. INISIALISASI VARIABEL NODE SAMA DENGAN n
# 5. LAKUKAN PERULANGAN KEMBALI, UNTUK n MULAI DARI Nn1 SAMPAI PANJANG ANAK
# 6. JIKA ANAK PADA INDEKS m LEBIH KECIL DARI ANAK PADA INDEKS NODE :
#       UBAH NODE SAMA DENGAN M
# 7. UBAH POSISI ANTAR ANAK INDEKS KE n DENGAN ANAK INDEKS KE NODE.
# 8. UBAH POSISI ANTAR ANAK INDEKS KE NODE DENGAN ANAK INDEKS KE n.
# 9. INISIALIASASI VARIBLE SOAL SAMA DENGAN 0
# 10. LAKUKAN PERULANGAN i MULAI DARI 0 SAMPAI SEPANJANG ANAK
# 11. JIKA ANAK INDEKS KE i TIDAK SAMA DENGAN ANAK INDEKS KE i+1 :
#       TAMBAHKAN ANAK INDEKS KE i+1 MINUS ANAK INDEKS KE i KE SOAL
# 12. KEMBALIKAN NILAI SOAL
# 13. INPUT JUMLAH ANAK
# 14. INPUT KEMAMPUAN ANAK DAN SIMPAN KE DALAM LIST ANAK
# 15. JIKA JUMLAH ANAK TIDAK GENAP, MAKA CETAK INPUT JUMLAH GENAP
# 16. JIKA TIDAK, PANGGIL FUNGSI DEF MINIMAL SOAL DAN MASUKKAN KEDALAM VARIABEL TOTAL MINIMAL SOAL
# 17. CETAK TOTAL MINIMAL SOAL
# 18.

# KOMPLEKSITAS = O(n^2)

def minimalSoal(anak):
    for n in range(len(anak)):
        node = n
        for m in range(n + 1, len(anak)):
            if anak[m] < anak[node]:
                node = m
        anak[n], anak[node] = anak[node], anak[n]

    soal = 0

    for i in range(0, len(anak), 2):
        if anak[i] != anak[i + 1]:
            soal += anak[i + 1] - anak[i]

    return soal


n = int(input("Jumlah anak : "))

anak = [int(x) for x in input("Kemampuan : ").split()]

if n % 2 != 0:
    print("Anda harus memasukkan jumlah anak yang genap!")
else:
    totalMinimalSoal = minimalSoal(anak)

    print(totalMinimalSoal)
