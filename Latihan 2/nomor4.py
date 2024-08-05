# ALGORITMA

# 1. IMPORT LIBRARY HEAPQ
# 2. INISIALISASI FUNGSI DEF JADWALKERJA DENGAN PARAMETER ORDERAN
# 	- INISIALISASI TEMPATORDERAN DENGAN LIST KOSONG
# 	- LAKUKAN PERULANGAN NAMA, KEUNTUNGAN, WAKTUJAHIT, WAKTUANTAR YANG ADA DI VARIABEL ORDERAN
# 	- TAMBAHKAN NILAINYA KEDALAM HEAP
# 	- INISIALISASI VARIABEL JADWAL DENGAN LIST KOSONG
# 	- INISIALISASI VARIABEL TOTALUNTUNG DENGAN NILAI 0
# 	- INISIALISASI VARIABEL DEADLINE DENGAN NILAI 0 DAN LAKUKAN PERULANGAN PADA ORDERAN DAN JUMLAHKAN DENGAN 1
# 	- LAKUKAN PERULANGAN TEMPATORDERAN
# 	- HAPUS NILAI AKHIR PADA VARIABEL MINUSUNTUNG, NAMA, WAKTUJAHIT, WAKTUANTAR MENGGUNAKAN HEAP
# 	- MASUKKAN NILAI MINUSUNTUNG KE DALAM VARIABEL KEUNTUNGAN
# 	- LAKUKAN PERULANGAN I SELAMA WAKTU ANTAR SAMPAI 0 DAN BERIKAN JEDANYA -1
# 	- JIKA INDEKS DEADLINE == 0, INDEKSNYA = 1
# 	- TAMBAHKAN NAMA KEDALAM JADWAL DAN TAMBAHKAN KEUNTUNGAN KE TOTALUNTUNG
# 	- BREAK
# 	- KEMBALIKAN NILAINYA
# 3. INPUT NILAI
# 4. INISIALISASI NILAI ORDERAN DENGAN LIST KOSONG
# 5. LAKUKAN PERULANGAN SELAMA N
# 	- INPUT NAMA, KEUNTUNGAN, WAKTUJAHIT, WAKTUANTAR DAN TETAPKAN DENGAN NILAI INT
# 	- TAMBAHKAN KE VARIABEL ORDERAN
# 	- PANGGIL FUNGSI JADWALKERJA
# 	- CETAK HASILJADWAL DAN HASILKEUNTUNGAN


# KOMPLEKSITAS WAKTU = O(N LOG N)
# KOMPLEKSITAS RUANG = O(N) + O(1)

import heapq


def jadwalKerja(orderan):
    tempatOrderan = []
    for nama, keuntungan, waktuJahit, waktuAntar in orderan:
        heapq.heappush(tempatOrderan, (-keuntungan, nama,
                       waktuJahit, waktuAntar))

    jadwal = []
    totalUntung = 0
    deadline = [0] * (max(x[3] for x in orderan) + 1)

    while tempatOrderan:
        minusUntung, nama, waktuJahit, waktuAntar = heapq.heappop(
            tempatOrderan)
        keuntungan = -minusUntung

        for i in range(waktuAntar, 0, -1):
            if deadline[i] == 0:
                deadline[i] = 1
                jadwal.append(nama)
                totalUntung += keuntungan
                break

    return jadwal, totalUntung


N = int(input().strip())

orderan = []
for _ in range(N):
    nama, keuntungan, waktuJahit, waktuAntar = input().strip().split()
    keuntungan = int(keuntungan)
    waktuJahit = int(waktuJahit)
    waktuAntar = int(waktuAntar)
    orderan.append((nama, keuntungan, waktuJahit, waktuAntar))

hasilJadwal, hasilKeuntungan = jadwalKerja(orderan)

print(" ".join(hasilJadwal))
print(hasilKeuntungan)
