#ALGORITMA
# Mulai
# Input huruf
# Inisialisasi variabel set dan panjangHuruf
# Buat perulangan koin di huruf kemudian tambahkan setiap inputan ke set dan hitung jumlah kemunculannya
# Lakukan perkondisian jika koin berada di 
# Inisialisasi variabel untuk menyimpan inputan yang berbeda dan posisinya
# Iterasi melalui inputan-inputan dalam input string
    # Jika inputan saat ini sama dengan inputan sebelumnya, lewati ke inputan berikutnya
    # Cek jika inputan saat ini adalah inputan yang berbeda
        # Jika inputan saat ini adalah inputan yang berbeda, update variabel
# Cetak posisi inputan yang berbeda
# Selesai

huruf = input()
 
set = set()
panjangHuruf = {}
 
for koin in huruf:
    set.add(koin)
    if koin in panjangHuruf:
        panjangHuruf[koin] += 1
    else:
        panjangHuruf[koin] = 1
 
banyakKoin = None
tempatKoin = -1
 
for i in range(len(huruf)):
    if i > 0 and huruf[i] == huruf[i-1]:
        continue
    if huruf[i] not in panjangHuruf or panjangHuruf[huruf[i]] == 1:
        banyakkoin = huruf[i]
        tempatKoin = i + 1
        break
 
print(tempatKoin)