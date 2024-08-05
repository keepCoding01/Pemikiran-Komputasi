# ALGORTIMA
# 1. buat fungsi def cariKombinasi dengan parameter angka dan tujuan
#    a. angka sebagai tempat bilangan acaknya
#    b. tujuan sebagai bilangan yang ingin dicari kombinasi penjumlahannya
# 2. inisialisasi variabel hasil
# 3. buat fungsi def nodeKembali dengan parameter kombinasi, sisa dan mulai
#    a. kombinasi sebagai tempat simpan kombinasi penjumlahan
#    b. sisa sebagai bilangan yang tersisa untuk dijumlahkan
#    c. mulai sebagai indeks awal untuk mulai
# 4. buat pengkondisian jika sisa == 0, maka kombinasi ditambahkan ke variabel hasil
# 5. lakukan perulangan i selama variabel mulai berjalan dan sepanjang angka
# 6. jika angka ke-i lebih besar dari sisa, break
# 7. tambahkan semua angka kedalam kombinasi
# 8. lakukan fungsi nodeKembali dan kemudian hapus elemen terakhir kombinasi
# 9. lakukan fungsi nodeKembali dan kembalikan variabel hasil
# 10. buat fungsi def main untuk inputan
# 11. inisialisasi var kombinasi dan lakukan perulangan untuk mencetak tiap angka
# 12. fungsi terakhir ialah jika program dieksekusi langsung disini, maka cetak

# kompleksitas waktu = O(v+e) + O(n)


def cariKombinasi(angka, tujuan):
    hasil = []

    def nodeKembali(kombinasi, sisa, mulai):

        if sisa == 0:
            hasil.append(kombinasi.copy())
            return

        for i in range(mulai, len(angka)):
            if angka[i] > sisa:
                break
            kombinasi.append(angka[i])
            nodeKembali(kombinasi, sisa - angka[i], i)
            kombinasi.pop()

    nodeKembali([], tujuan, 0)
    return hasil


def main():
    angka = [int(x)
             for x in input("Masukkan bilangan acak: ").split()]
    tujuan = int(
        input("Masukkan bilangan yang ingin dicari kombinasi penjumlahannya: "))

    kombinasi = cariKombinasi(angka, tujuan)

    print("Semua kemungkinan penjumlahan:")
    for kombinasi in kombinasi:
        print(" ".join(str(x) for x in kombinasi))


if __name__ == "__main__":
    main()
