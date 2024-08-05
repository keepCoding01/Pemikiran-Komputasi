# ALGORITMA
# 1. IMPORT HEAPQ, RANDOM, DATETIME, TIMEDELTA, TABULATE, FRACTION.
# 2. BUAT LIST STASIUN, DICT SELURUH RUTE DAN DICT KERETAAPI DIDALAM LIST.
# 3. INISIALISASI DEF DJIKSTRA DENGAN 3 PARAMETER (RUTE, AWAL, AKHIR).
# 	- INISIALISASI QUEUE DENGAN LIST YANG MENGISI TIAP PARAMETER DJIKSTRA.
# 	- SET TELAHDIKUNJUNGI DENGAN FUNGSI SET().
# 	- LAKUKAN PERULANGAN QUEUE SELAMA KONDISI TERPENUHI.
# 	- INISIALISASI DURASIRUTE, STASIUN, JALUR KE DALAM VARIABEL QUEUE YANG TELAH DIBUAT SEBELUMNYA UNTUK MENYIMPAN NILAI MASING-MASING.
# 	- JIKA STASIUN TERMASUK DALAM TELAHDIKUNJUNGI, TERUSKAN PROGRAM.
# 	- TAMBAHKAN STASIUN KE DALAM TELAHDIKUNJUNGI.
# 	- TAMBAHKAN JALUR DENGAN STASIUN UNTUK DIMASUKKAN NILAINYA KE DALAM JALUR.
# 	- JIKA STASIUN == AKHIR, KEMBALIKAN NILAI DURASIRUTE DAN JALUR.
# 	- SELAMA STASIUNBERIKUTNYA DAN JARAK BERADA DIDALAM RUTE, AMBIL NILAI STASIUN PER-ITEM.
# 	- JIKA STASIUNBERIKUTNYA TIDAK ADA DI TELAHDIKUNJUNGI, TAMBAHKAN NILAI YANG ADA DIDALAM DURASIRUTE+JARAK, STASIUNBERIKUTNYA, JALUR KE DALAM QUEUE DAN TAMBAHKAN KE BAGIAN BELAKANG.
# 	- KEMBALIKAN NILAINYA.
# 4. INISIALISASI DEF VIEWTRAIN.
# 	- LAKUKAN PERULANGAN SELAMA KONDISI BENAR.
# 	- INISIALISASI TABEL.
# 	- LAKUKAN PERULANGAN KERETA SELAMA NILAI YANG ADA DIDALAM VARIABLE KERETA API.
# 	- BUAT TABEL MENGGUNAKAN TABULATE.
# 	- JIKA PENGGUNA TIDAK INGIN DIBERIKAN REKOMENDASI BARANGNBAWAAN ALIAS MENGINPUT "TIDAK" MAKA BERIKAN STEP BERIKUTNYA YAITU TANYAKAN KELAS KERETA API DAN KEMUDIAN KELUAR DARI MENU VIEWTRAIN.
# 	- JIKA PENGGUNA MENGINPUT DATA YANG SALAH (DILUAR DARI KATA YA/TIDAK), BERIKAN KESEMPATAN UNTUK MENGULANG YANG BENAR.
# 	- JIKA PENGGUNA INGIN DIBERIKAN REKOMENDASI BARANGBAWAAN ALIAS MENGINPUT "YA", MAKA BERIKAN STEP BERIKUTNYA YAITU TANYAKAN KELAS KERETA API YANG INGIN DICOBA.
# 	- CETAK PENJELASAN UNTUK MEMBERIKAN NILAI PRIORITAS MASING-MASING BARANG.
# 	- TANYAKAN BERAPA BANYAK BARANG YANG INGIN DIBAWA.
# 	- LAKUKAN PERULANGAN I SEPANJANG JUMLAHBARANG + 1.
# 	- CETAK FORMAT UNTUK MEMBUAT DATA BARANG KEMUDIAN MASUKKAN KE BARANGBARANG.
# 	- CETAK DAN INPUT APAKAH BARANG INGIN DIPECAH?.
# 	- JIKA YA, MAKA LANJUTKAN FUNGSI FRACTIONALKNAPSACK.
# 	- JIKA TIDAK, MAKA LANJUTKAN FUNGSI ONEZEROKNAPSACK.
# 	- TANYAKAN APAKAH INGIN MENCOBA KELAS LAIN?
# 	- JIKA YA, MAKA ULANGI DEF VIEWTRAIN, JIKA TIDAK MAKA PROGRAM BERHENTI.
# 5. INISIALISASI DEF ONEZEROKNAPSACK DENGAN 2 PARAMETER (KERETATERPILIH,BARANGBARANG)
# 	- INISIALISASI NILAI TOTALBERAT = 0
# 	- INISIALISASI NILAI TOTALNILAI = 0
# 	- INISIALISASI NILAI REKOMENDASIBARANG DENGAN LIST KOSONG
# 	- LAKUKAN PERULANGAN NAMA,BERAT,PRIORITAS SELAMA NILAINYA ADA DI VARIABEL BARANGBARANG.
# 	- JIKA KERETATERPILIH LEBIH KECIL SAMA DENGAN 0, HENTIKAN.
# 	- JIKA BERAT <= KERETATERPILIH, TAMBAHKAN BERAT KE VARIABEL TOTALBERAT DAN TAMBAHKAN NILAI PRIORITAS KE DALAM VARIABEL TOTALNILAI.
# 	- TAMBAHKAN NAMA KE DALAM REKOMENDASIBARANG.
# 	- KURANGKAN BERAT DENGAN NILAI KERETATERPILIH KEMUDIAN MASUKKAN NILAINYA DI KERETATERPILIH.
# 	- CETAK KAMI MEREKOMENDASIKAN KAMU UNTUK MEMBAWA :.
# 	- LAKUKAN PERULANGAN UNTUK MENCETAK NOMOR DAN NAMA BARANG.
# 	- CETAK BERAT TOTAL BARANG YANG DIBAWA DARI NILAI YANG ADA DI VARIABEL TOTAL BERAT.
# 6. INISIALISASI DEF FRACTIONALKNAPSACK DENGAN 2 PARAMETER (KERETATERPILIH, BARANGBARANG).
# 	- MENGURUTKAN BARANG BARANG.
# 	- INISIALISASI VARIABEL TOTALBERAT DAN TOTALNILAI DENGAN NILAI 0.
# 	- INISIALISASI VARIABEL REKOMENDASIBARANG DENGAN LIST KOSONG.
# 	- LAKUKAN PERULANGAN NAMA,BERAT,PRIORITAS SELAMA NILAINYA ADA DI BARANGBARANG.
# 	- JIKA BERAT LEBIH KECIL SAMA DENGAN  KERETATERPILIH, KURANGKAN BERATNYA DAN TAMBAHKAN BERAT KE TOTAL BERAT SERTA PRIORITAS KE TOTAL NILAI.
# 	- TAMBAHKAN NILAI YANG ADA DI VARIABEL NAMA DIIKUTI DENGAN KATA UTUH DI REKOMENDASIBARANG.
# 	- JIKA TIDAK, INISIASLISASI NILAI BARANGTERBAIK DENGAN NONE DAN URUTKAN BARANGBARANG.
# 	- SELAMA ITEM ADA DI MENGURUTKANBARANG, JIKA ITEM PADA INDEKS PERTAMA LEBIH KECIL DARI KERETATERPILIH, HITUNG FRAKSINYA.
# 	- MASUKKAN NILAI BERATYANGDIAMBIL KE DALAM TOTALBERAT.
# 	- MASUKKAN HASIL PERKALIAN DARI ITEM PADA INDEKS KEDUA DENGAN FRAKSI KE DALAM TOTALNILAI.
# 	- JIKA FRAKSI SAMA DENGAN 1, MAKA CETAK UTUH. JIKA TIDAK MAKA CETAK NILAI PECAHAN MENGGUNAKAN LIBRARY FRACTION.
# 	- TAMBAHKAN NILAINYA KEDALAM VARIABEL REKOMENDASI BARANG.
# 	- KURANGKAN NILAI ITEM DI INDEKS PERTAMA DENGAN BERAT YANG DIAMBIL DAN MASUKKAN KEDALAM SISABERAT.
# 	- JIKA SISABERAT > 0, HAPUS ITEM BARANGBARANG DAN ITEM INDEKS-0, SISABERAT DAN ITEM PADA INDEKS-2, KE SISABERAT.
# 	- HENTIKAN PROGRAM.
# 	- JIKA BARANGTERBAIK, LAKUKAN PENGURANGAN INDEKS PERTAMA-1 PADA BARANGTERBAIK DAN TAMBAHKAN KEDALAM KERETATERPILIH.
# 	- TAMBAHKAN INDEKS-1 BARANGTERBAIK KE TOTALBERAT DAN TAMBAH INDEKS-2 BARANGTERBAIK KE TOTALNILAI.
# 	- MASUKKAN INDEKS KE NOL DENGAN KATA UTUH KEDALAM REKOMENDASIBARANG.
# 	- JIKA TIDAK, MASUKKAN NILAI DARI KERETATERPILIH KEDALAM SISAKAPASITAS.
# 	- BAGI NILAI SISAKAPASITAS DENGAN BERAT DAN MASUKKAN NILAINYA KEDALAM VARIABEL FRAKSI.
# 	- KALIKAN NILAI FRAKSI DENGAN BERAT DAN TAMPUNG NILAINYA KE DALAM BERATYANGDIAMBIL.
# 	- TAMBAHKAN NILAI BERATYANGDIAMBIL KE DALAM VARIBEL TOTALBERAT.
# 	- TAMBAHKAN HASIL PERKALIAN FRAKSI DENGAN PRIORITAS KE DALAM VARIABEL TOTALNILAI.
# 	- MASUKKAN NILAI NAMA DAN FRAKSI KE DALAM REKOMENDASIBARANG.
# 	- KURANGKAN NILAI BERATYANGDIAMBIL DENGAN KERETATERPILIH.
# 	- LAKUKAN PERULANGAN ITEM SELAMA NILAINYA ADA PADA BARANGBARANG.
# 	- JIKA ITEM PADA INDEKS PERTAMA LEBIH KECIL SAMA DENGAN KERETATERPILIH, HAPUS ITEM PADA BARANGBARANG DAN MASUKKAN KEMBALI PADA POSISI PERTAMA.
# 	- JIKA KERETATERPILIH BUKAN LEBIH BESAR DARI NOL, HENTIKAN PROGRAM TERSEBUT.
# 	- CETAK KAMI MEREKOMENDASI BARANG YANG DAPAT DIBAWA.
# 	- LAKUKAN PERULANGAN UNTUK MENCETAK HASILNYA.
# 	- CETAK BERAT TOTAL BARANG YANG DIBAWA.
# 7. INISIALISASI FUNGSI VIEWROUTES.
# 	- INISIASASI STASIUNS DENGAN LIST UNTUK RUTE ALIAS AMBIL NILAI KEYNYA.
# 	- INISIALISASI VARIABEL TELAHDITAMPILKAN DENGAN NILAI SET.
# 	- INISIALISASI VARIABEL UNTUK TABEL.
# 	- LAKUKAN PERULANGAN SELAMA AWAL ADA NILAINYA DI STASIUNS.
# 	- LAKUKAN PERULANGAN AKHIR DARI INDEKS AWAL DI RUTE.
# 	- JIKA VAR AWAL DAN AKHIR TIDAK ADA DI TELAHDITAMPILKAN, BEGITU JUGA SEBALIKNYA, INISIALISASI DURASIRUTE UNTUK MENAMPUNG NILAI RUTE DI INDEKS AWAL DAN AKHIR.
# 	- INISIALISASI TABEL DENGAN FUNGSI TABULATE UNTUK MENCETAK RUTE DAN DURASI.
# 	- LAKUKAN PERULANGAN SELAMA KONDISI BENAR.
# 	- CETAK MASUKKAN RUTE KAMU.
# 	- INPUT NILAI STASIUNASAL DAN TUJUAN.
# 	- JIKA STASIUNASAL TIDAK ADA DI DAFTAR STASIUNS, CETAK STASIUN TIDAK VALID. SILAKAN COBA LAGI.
# 	- PANGGIL FUNGSI DJIKSTRA DAN TAMPUNG NILAINYA DI VARIABEL DURASIRUTE DAN JALUR.
# 	- JIKA DURASIRUTE NILAINYA TAK HINGGA, CETAK TIDAK ADA RUTE YANG TERSEDIA.
# 	- JIKA TIDAK, PRINT JALUR TERPENDEKNYA.
# 	- JIKA INPUT LIHAT RUTE LAIN BUKAN 'YA', HENTIKAN PROGRAM TERSEBUT.
# 8. INISIALISASI DEF ORDERTICKET.
# 	- CETAK PASTIKAN ANDA TELAH MEMERIKSA RUTE SEBELUM MEMESAN TIKET DAN TANYAKAN KEMANA AKAN PERGI.
# 	- INPUT NILAI STASIUNASAL DAN TUJUAN.
# 	- JIKA STASIUN ASAL TIDAK ADA DI DAFTAR STASIUN, CETAK STASIUN TIDAK VALID DAN KEMBALIKAN NILANYA.
# 	- PANGGIL FUNGSI DJIKSTRA DAN TAMPUNG KE DALAM VARIABEL DURASIRUTE DAN JALUR.
# 	- JIKA NILAI DURASIRUTE INF, CETAK TIDAK ADA RUTE YANG TERSEDIA DAN KEMBALIKAN NILAI.
# 	- CETAK RUTE PERJALANAN TERPENDEK.
# 	- LAKUKAN PERULANGAN SELAMA KONDISI BENAR.
# 	- CETAK PASTIKAN ANDA TELAH MEMERIKSA BARANGBAWAAN ANDA SEBELUM MEMILIH KELAS.
# 	- INPUT NILAI KELASKERETAAPI.
# 	- JIKA TULISANNYA LOWER SEMUA, MAKA CAPITALIZE DAN BREAK.
# 	- JIKA TIDAK, CETAK KELAS KERETA YANG ANDA MASUKKAN SALAH. SILAKAN COBA LAGI.
# 	- CETAK SILAKAN MASUKKAN DATA ANDA.
# 	- MASUKKAN DATA NAMA, TANGGAL, WAKTU DAN KONFIRMASI.
# 	- INISIALISASI NOMORKERETA, KERETA, PLATFORM, KURSI DENGAN NILAI ACAK MENGGUNAKAN FUNGSI RANDOM.
# 	- INISIALISASI FORMAT WAKTUTIBA DAN WAKTUPERJALANAN.
# 	- INISIALISASI WAKTUPERJALANAN DENGAN TP DAN WP.
# 	- INISIALISASI WAKTUTIBA DENGAN TT DAN WT.
# 	- HITUNG TOTALBIAYA DENGAN MENGALIKAN 15 DENGAN DURASIRUTE + KERETA.
# 	- JIKA KONFIRMASI SAMA DENGAN 'YA', CETAK FORMAT TIKET.
# 	- CETAK TOTAL BIAYA MELALUI VARIABEL TOTALBIAYA.
# 	- JIKA PESAN TIKET LAGI DIINPUT YA, MAKA JALANKAN KEMBALI DEF ORDERTICKET.
# 	- JIKA BUKAN, MAKA BERHENTI DAN CETAK PEMESANAN TIKET DIBATALKAN. SILAKAN COBA LAGI.
# 9. INISIALISASI DEF MENUUTAMA.
# 	- CETAK SELAMAT DATANG DI PROGRAM PEMESANAN TIKET KERETA API.
# 	- INPUT NAMA DEPAN.
# 	- LAKUKAN PERULANGAN SELAMA KONDISI BENAR.
# 	- CETAK SELAMAT DATANG DI (NAMA KITA) EXPRESS.
# 	- CETAK SEMUA MENU (PESAN TIKET, LIHAT RUTE, LIHAT KERETA, KELUAR).
# 	- INPUT UNTUK MEMILIH PILIHAN MENU.
# 	- JIKA MEMILIH 1, JALANKAN FUNGSI ORDERTICKET.
# 	- JIKA MEMILIH 2, JALANKAN FUNGSI VIEWROUTES.
# 	- JIKA MEMILIH 3, JALANKAN FUNGSI VIEWTRAIN.
# 	- JIKA MEMILIH 4, CETAK TERIMA KASIH TELAH MENGGUNAKAN PROGRAM KAMI. HENTIKAN PROGRAM.
# 	- JIKA BUKAN SEMUANYA, CETAK PILIHAN TIDAK VALID. SILAKAN COBA LAGI.
# 10. JALANKAN FUNGSI MENUUTAMA.

# TOTAL KOMPLEKSITAS WAKTU
# T(n) = O((V + E)log V + n log n)
# CATATAN :
# PADA SETIAP FUNGSI, AKAN DIPILIH WAKTU YANG PALING EFEKTIF DAN EFISIEN.
# FUNGSI YANG PALING BAGUS ADA DI ALGORITMA DJIKSTRA DAN FRACTIONAL KNAPSACK DI DALAM MENU orderTicket(), viewRoutes() DAN 'viewTrain()'.
# SEHINGGA, KOMPLEKSITAS WAKTU SECARA KESELURUHAN YANG DIDAPAT MERUPAKAN PENGGABUNGAN ANTARA ALGORITMA DJIKSTRA DAN FRACTIONAL KNAPSACK.


# TOTAL KOMPLEKSITAS RUANG
# S(n) = O(V + E + n)
# PADA SETIAP FUNGSI, AKAN DIPILIH RUANG YANG PALING BESAR.
# FUNGSI DENGAN PENGGUNAAN RUANG TERBESAR ADA PADA  djikstra(), viewRoutes(), oneZeroKnapsack() DAN fractionalKnapsack().
# SEHINGGA,KOMPLEKSITAS RUANG SECARA KESELURUHAN YANG DIDAPAT MERUPAKAN PENGGABUNGAN ANTARA KEEMPAT FUNGSI TERSEBUT.


import heapq
import random
from datetime import datetime, timedelta
# jika ingin menggunakan kode program ini, pastikan sudah menginstall "pip install tabulate" di terminal.
from tabulate import tabulate
# import fraction ini, bukan berarti langsung membagi menjadi pecahan. namun merubah bilangan desimal (0,5) menjadi pecahan (1/2).
from fractions import Fraction

stasiuns = ['Minstowe', 'Oldcastle', 'Cowstone',
            'New North', 'Freeham', 'Bingborough', 'Donningpool', 'Old Mere', 'Highbrook', 'Wington']
rute = {
    "Minstowe": {"Cowstone": 3},
    "Oldcastle": {"New North": 5, "Freeham": 2},
    "Cowstone": {"Minstowe": 3, "New North": 4, "Bingborough": 6, "Donningpool": 7, "Highbrook": 5, "Freeham": 2},
    "New North": {"Oldcastle": 5, "Cowstone": 4, "Bingborough": 3, "Donningpool": 6, "Wington": 4, "Highbrook": 2},
    "Freeham": {"Oldcastle": 2, "Cowstone": 2, "Donningpool": 3, "Wington": 5},
    "Bingborough": {"Cowstone": 6, "New North": 3, "Donningpool": 2, "Highbrook": 1},
    "Donningpool": {"Cowstone": 7, "New North": 6, "Freeham": 3, "Bingborough": 2, "Wington": 4, "Highbrook": 5, "Old Mere": 2},
    "Highbrook": {"Cowstone": 5, "New North": 2, "Bingborough": 1, "Donningpool": 5},
    "Wington": {"New North": 4, "Freeham": 5, "Donningpool": 4},
    "Old Mere": {"Donningpool": 2}
}

keretaApi = [
    {'namaKelasKeretaApi': 'Economy',
        'kapasitasKeretaApi': 25, 'hargaKelasKeretaApi': 20},
    {'namaKelasKeretaApi': 'Business',
        'kapasitasKeretaApi': 30, 'hargaKelasKeretaApi': 30},
    {'namaKelasKeretaApi': 'Exclusive',
        'kapasitasKeretaApi': 35, 'hargaKelasKeretaApi': 40}
]


# T(n) = O((V + E)log V)
# S(n) = O(V)
def dijkstra(rute, awal, akhir):
    queue = [(0, awal, [])]
    telahDikunjungi = set()
    while queue:
        durasiRute, stasiun, jalur = heapq.heappop(queue)
        if stasiun in telahDikunjungi:
            continue
        telahDikunjungi.add(stasiun)
        jalur = jalur + [stasiun]
        if stasiun == akhir:
            return durasiRute, jalur
        for stasiunBerikutnya, jarak in rute.get(stasiun, {}).items():
            if stasiunBerikutnya not in telahDikunjungi:
                heapq.heappush(
                    queue, (durasiRute + jarak, stasiunBerikutnya, jalur))
    return float("inf"), []


# T(n) = O(n)
# S(n) = O(n)
def viewTrain():
    while True:
        tabel = []
        for kereta in keretaApi:
            tabel.append([kereta['namaKelasKeretaApi'],
                         kereta['kapasitasKeretaApi'], kereta['hargaKelasKeretaApi']])
        print(tabulate(tabel, headers=[
              'Nama Kereta', 'Kapasitas Bagasi (kg)', 'Harga ($) per kg'], tablefmt="grid"))
        barangBawaan = input(
            "kamu bisa membantu kamu memilih apa yang akan dibawa, apakah kamu ingin mencoba ?\nya/tidak = ")
        if barangBawaan == "tidak":
            while True:
                kelasKereta = input("Pilih kelas : ").capitalize()
                if kelasKereta in ['Economy', 'Business', 'Exclusive']:
                    break
                else:
                    print(
                        "Kelas kereta yang Anda pilih tidak valid. Silakan coba lagi.")

            keretaTerpilih = next(
                (kereta for kereta in keretaApi if kereta['namaKelasKeretaApi'] == kelasKereta), None)

            if not keretaTerpilih:
                print("Kelas kereta yang Anda pilih tidak tersedia.")
                return

            keretaTerpilih = keretaTerpilih.copy()
            break

        elif barangBawaan not in ["tidak", "ya"]:
            print("kamu salah input. coba lagi")
            viewTrain()

        while True:
            kelasKereta = input("Pilih kelas : ").capitalize()
            if kelasKereta in ['Economy', 'Business', 'Exclusive']:
                break
            else:
                print("Kelas kereta yang Anda pilih tidak valid. Silakan coba lagi.")

        keretaTerpilih = next(
            (kereta for kereta in keretaApi if kereta['namaKelasKeretaApi'] == kelasKereta), None)

        if not keretaTerpilih:
            print("Kelas kereta yang Anda pilih tidak tersedia.")
            return

        keretaTerpilih = keretaTerpilih.copy()

        if barangBawaan == "ya":
            barangBarang = []
            print(
                "Berikan skala prioritas barang kamu mulai dari 1 (sangat penting) sampai 5 (tidak penting)")
            jumlahBarang = int(
                input("Berapa banyak barang yang ingin kamu bawa? "))

            for i in range(1, jumlahBarang + 1):
                print(f"\nBarang-{i}")
                nama = input(f"Nama barang-{i}: ")
                berat = float(input(f"Berat barang-{i} (kg): "))
                prioritas = int(input(f"Prioritas barang-{i} (1-5): "))
                barangBarang.append((nama, berat, prioritas))
            bisaDipecah = input(
                "Apakah barang ingin kamu pecah menjadi beberapa bagian? (ya/tidak): ").lower() == 'ya'

            if bisaDipecah:
                fractionalKnapsack(keretaTerpilih, barangBarang)
            else:
                oneZeroKnapsack(keretaTerpilih, barangBarang)

        if input("\nApakah ingin mencoba kelas lain? (ya/tidak): ").lower() != 'ya':
            break


# T(n) = O(n)
# S(n) = O(n)
def oneZeroKnapsack(keretaTerpilih, barangBarang):
    totalBerat = 0
    totalNilai = 0
    rekomendasiBarang = []

    for nama, berat, prioritas in barangBarang:
        if keretaTerpilih['kapasitasKeretaApi'] <= 0:
            break

        if berat <= keretaTerpilih['kapasitasKeretaApi']:
            totalBerat += berat
            totalNilai += prioritas

            rekomendasiBarang.insert(0, (nama))
            keretaTerpilih['kapasitasKeretaApi'] -= berat

    print("\nKami merekomendasikan kamu untuk membawa :")
    for idx, item in enumerate(rekomendasiBarang, start=1):
        print(f"{idx}. {item}")
    print(f"\nBerat total barang yang dibawa: {totalBerat} kg")


# T(n) = O(n log n)
# S(n) = O(n)
def fractionalKnapsack(keretaTerpilih, barangBarang):
    barangBarang.sort(key=lambda x: x[1], reverse=True)

    totalBerat = 0
    totalNilai = 0
    rekomendasiBarang = []

    for nama, berat, prioritas in barangBarang:
        if keretaTerpilih['kapasitasKeretaApi'] > 0:
            if berat <= keretaTerpilih['kapasitasKeretaApi']:
                keretaTerpilih['kapasitasKeretaApi'] -= berat
                totalBerat += berat
                totalNilai += prioritas
                rekomendasiBarang.append((nama, "utuh"))
            else:
                barangTerbaik = None
                mengurutkanBarang = sorted(
                    barangBarang, key=lambda x: x[1])
                for item in mengurutkanBarang:
                    if item[1] <= keretaTerpilih['kapasitasKeretaApi']:
                        fraksi = min(
                            1, keretaTerpilih['kapasitasKeretaApi'] / item[1])
                        beratYangDiambil = fraksi * item[1]
                        totalBerat += beratYangDiambil
                        totalNilai += item[2] * fraksi
                        if fraksi == 1:
                            labelFraksi = "utuh"
                        else:
                            labelFraksi = str(
                                Fraction(fraksi).limit_denominator())

                        rekomendasiBarang.append(
                            (item[0], labelFraksi))
                        keretaTerpilih['kapasitasKeretaApi'] -= beratYangDiambil

                        sisaBerat = item[1] - beratYangDiambil
                        if sisaBerat > 0:
                            barangBarang.remove(item)
                            barangBarang.append(
                                (item[0], sisaBerat, item[2]))

                        break

                if barangTerbaik:
                    keretaTerpilih['kapasitasKeretaApi'] -= barangTerbaik[1]
                    totalBerat += barangTerbaik[1]
                    totalNilai += barangTerbaik[2]
                    rekomendasiBarang.append(
                        (barangTerbaik[0], "utuh"))
                    barangBarang.remove(barangTerbaik)
                else:
                    sisaKapasitas = keretaTerpilih['kapasitasKeretaApi']
                    fraksi = sisaKapasitas / berat
                    beratYangDiambil = fraksi * berat
                    totalBerat += beratYangDiambil
                    totalNilai += prioritas * fraksi
                    rekomendasiBarang.append(
                        (nama, str(Fraction(round(fraksi, 2)).limit_denominator())))
                    keretaTerpilih['kapasitasKeretaApi'] -= beratYangDiambil

                    for item in barangBarang:
                        if item[1] <= keretaTerpilih['kapasitasKeretaApi']:
                            barangBarang.remove(item)
                            barangBarang.insert(0, item)
                            break

        else:
            break

    print("\nKami merekomendasi barang yang dapat kamu bawa :")

    for idx, item in enumerate(rekomendasiBarang, start=1):
        namaBarang = item[0].capitalize()
        labelFr = item[1]

        if labelFr == "utuh":
            print(f"{idx}. {namaBarang} (utuh)")
        else:
            print(f"{idx}. {namaBarang} ({labelFr})")
    print(f"\nBerat total barang yang dibawa: {totalBerat} kg")


# T(n) = O(V + E)
# S(n) = O(V + E)
def viewRoutes():
    stasiuns = list(rute.keys())
    telahDitampilkan = set()
    tabel = []
    for awal in stasiuns:
        for akhir in rute[awal]:
            if (awal, akhir) not in telahDitampilkan and (akhir, awal) not in telahDitampilkan:
                durasiRute = rute[awal][akhir]
                tabel.append([f"{awal} -- {akhir}", durasiRute])
                telahDitampilkan.add((awal, akhir))
    print("Biaya : $15/jam")
    print(tabulate(tabel, headers=[
          "Routes (2-jalan)", "Durasi (jam)"], tablefmt="outline"))

    while True:
        print("Masukkan rute kamu")
        print("====================")
        stasiunAsal = input("\nDari : ")
        stasiunTujuan = input("Ke   : ")
        if stasiunAsal not in stasiuns or stasiunTujuan not in stasiuns:
            print("Stasiun tidak valid. Silakan coba lagi.")
            continue

        durasiRute, jalur = dijkstra(rute, stasiunAsal, stasiunTujuan)
        if durasiRute == float("inf"):
            print("Tidak ada rute yang tersedia.")
        else:
            print(
                f"Ini adalah rute terpendek dari {stasiunAsal} ke {stasiunTujuan}:\n{' -> '.join(jalur)}\nDurasi: {durasiRute} jam")

        if input("\nLihat rute lain? (ya/tidak): ").lower() != 'ya':
            break


# T(n) = O(1)
# S(n) = O(V)
def orderTicket():
    print("Pastikan Anda telah memeriksa rute sebelum memesan tiket.\nkemana kamu akan pergi ?")
    stasiunAsal = input("Dari : ")
    stasiunTujuan = input("Ke   : ")
    if stasiunAsal not in stasiuns or stasiunTujuan not in stasiuns:
        print("Stasiun tidak valid.")
        return

    durasiRute, jalur = dijkstra(rute, stasiunAsal, stasiunTujuan)
    if durasiRute == float("inf"):
        print("Tidak ada rute yang tersedia.")
        return

    print(
        f"\nIni adalah rute perjalanan dari {stasiunAsal} ke {stasiunTujuan}: \n{' -> '.join(jalur)} \nDurasi: {durasiRute} jam")

    while True:
        print("\nPastikan Anda telah memeriksa barang bawaan Anda sebelum memilih kelas.")
        kelasKeretaInput = input(
            "Pilih kelas (Ekonomi, Bisnis, Eksekutif): ")
        if kelasKeretaInput.lower() in ['ekonomi', 'bisnis', 'eksekutif']:
            kelasKereta = kelasKeretaInput.capitalize()
            break
        else:
            print("Kelas kereta yang Anda masukkan salah. Silakan coba lagi.")

    print("\nSilakan masukkan data Anda : ")
    nama = input("Masukkan nama Anda\t\t\t\t: ")
    tanggal = input("Masukkan tanggal keberangkatan (DD/MM/YYYY)\t: ")
    waktu = input("Masukkan waktu keberangkatan (HH:MM)\t\t: ")
    konfirmasi = input("Apakah data Anda sudah benar? (ya/tidak)\t: ")

    nomorKereta = random.randint(000, 999)
    kereta = random.choice(keretaApi)
    platform = f"{random.randint(1, 10):02}"
    kursi = random.randint(1, 50)
    waktuTiba = datetime.strptime(
        tanggal + ' ' + waktu, '%d/%m/%Y %H:%M') + timedelta(hours=durasiRute)
    waktuPerjalanan = datetime.strptime(
        tanggal + ' ' + waktu, '%d/%m/%Y %H:%M')

    tp = waktuPerjalanan.strftime(
        '%d/%m/%Y')
    wp = waktuPerjalanan.strftime('%H:%M')
    tt = waktuTiba.strftime('%d/%m/%Y')
    wt = waktuTiba.strftime('%H:%M')
    totalBiaya = 15 * durasiRute + kereta['hargaKelasKeretaApi']

    if konfirmasi.lower() == 'ya':
        print(f'''
+------------------------------------------------------------+
| TIKET KERETA API MELLOW                                    |
+------------------------------------------------------------+
| ASAL     : {stasiunAsal}                                        |
| TANGGAL  : {tp}                  WAKTU : {wp}       |
| KERETA   : {nomorKereta}                        KELAS : {kelasKereta}    |
| PLATFORM : {platform}                          KURSI : {kursi}          |
+------------------------------------------------------------+
| TUJUAN   : {stasiunTujuan}                                        |
+------------------------------------------------------------+
| TANGGAL TIBA   : {tt}            WAKTU TIBA : {wt}  |
+------------------------------------------------------------+
| NAMA PENUMPANG : {nama}                                     |
+------------------------------------------------------------+
''')
        print(f"Total biaya : ${totalBiaya}")
        if input("\nPesan tiket lagi? (ya/tidak): ").lower() != 'ya':
            pass
        else:
            orderTicket()
    else:
        print("\nPemesanan tiket dibatalkan. Silakan coba lagi.")


# T(n) = Tergantung fungsi yang dipanggil dalam loop
# S(n) = Tergantung fungsi yang dipanggil
def menuUtama():
    print("================================================================")
    print("Selamat datang di program pemesanan tiket Kereta Api")
    nama = input("\nSebelum menggunakan program, masukkan nama depan Anda : ")
    print("================================================================")
    while True:
        print(f"\nSelamat datang di {nama} Express")
        print("===================================")
        print("1. Pesan Tiket")
        print("2. Lihat Rute")
        print("3. Lihat Kereta")
        print("4. Keluar")
        print("===================================")
        pilihan = input("Pilih (1-4): ")

        if pilihan == '1':
            orderTicket()
        elif pilihan == '2':
            viewRoutes()
        elif pilihan == '3':
            viewTrain()
        elif pilihan == '4':
            print("Terima kasih telah menggunakan program kami.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


menuUtama()
