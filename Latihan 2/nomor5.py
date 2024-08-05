# ALGORITMA

# 1. INISIALISASI FUNGSI DEF KESENANGAN DENGAN PARAMETER N DAN NILAI
# 	- JIKA N == 0, KEMBALIKAN NILAI 0
# 	- JIKA N == 1, KEMBALIKAN NILAI INDEKS KE-0
# 	- INISIALISASI TEMPAT1 DENGAN NILAI INDEKS KE-0
# 	- INISIALISASI TEMPAT2 DENGAN NILAI INDEKS KE-0 DAN KE-1
# 	- INISIALISASI I = 2
# 	- LAKUKAN PERULANGAN SELAMA I < N
# 	- INISIALISASI VARIABEL SEKARANG DENGAN NILAI MAX TEMPAT2 DAN TEMPAT1 + INDEKS I PADA NILAI
# 	- UBAH NILAI TEMPAT1 = TEMPAT2
# 	- UBAH NILAI TEMPAT2 = SEKARANG
# 	- TAMBAH 1 UNTUK MASING-MASING NILAI I
# 	- KEMBALIKAN NILAIN TEMPAT2
# 2. INPUT NILAI JLHPULAU
# 3. INISIALISASI NILAI DENGAN LIST KOSONG
# 4. INPUT NILAI
# 5. LAKUKAN PERULANGAN DENGAN NILAI YANG DIINPUT KE VARIABEL PULAU DAN TAMBAHKAN KE DALAM VARIABEL NILAI
# 6. PANGGIL FUNGSI KESENANGAN
# 7. CETAK HASIL


# KOMPLEKSITAS WAKTU: O(N)
# KOMPLEKSITAS RUANG: 0(N)


def kesenangan(n, nilai):
    if n == 0:
        return 0
    if n == 1:
        return nilai[0]

    tempat1 = nilai[0]
    tempat2 = max(nilai[0], nilai[1])

    i = 2
    while i < n:
        sekarang = max(tempat2, tempat1 + nilai[i])
        tempat1 = tempat2
        tempat2 = sekarang
        i += 1

    return tempat2


jlhPulau = int(input().strip())

nilai = []
masukanNilai = input().strip().split()
for pulau in masukanNilai:
    nilai.append(int(pulau))


print(kesenangan(jlhPulau, nilai))
