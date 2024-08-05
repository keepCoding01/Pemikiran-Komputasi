# ALGORTIMA
# 1. mulai
# 2. buat fungsi def cariKombinasi dengan parameter angka dan tujuan
#    a. angka sebagai tempat bilangan acaknya
#    b. tujuan sebagai bilangan yang ingin dicari kombinasi penjumlahannya
# 3. inisialisasi variabel hasil
# 4. buat fungsi def nodeKembali dengan parameter kombinasi, sisa dan mulai
#    a. kombinasi sebagai tempat simpan kombinasi penjumlahan
#    b. sisa sebagai bilangan yang tersisa untuk dijumlahkan
#    c. mulai sebagai indeks awal untuk mulai
# 5. buat pengkondisian jika sisa == 0, maka kombinasi ditambahkan ke variabel hasil
# 6. lakukan perulangan i selama variabel mulai berjalan dan sepanjang angka
# 7. jika angka ke-i lebih besar dari sisa, break
# 8. tambahkan semua angka kedalam kombinasi
# 9. lakukan fungsi nodeKembali dan kemudian hapus elemen terakhir kombinasi
# 10. lakukan fungsi nodeKembali dan kembalikan variabel hasil
# 11. buat fungsi def main untuk inputan
# 12. inisialisasi var kombinasi dan lakukan perulangan untuk mencetak tiap angka
# 13. fungsi terakhir ialah jika program dieksekusi langsung disini, maka cetak
 
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
    angka = [int(x) for x in input().split()]
    tujuan = int(input())
 
    kombinasi = cariKombinasi(angka, tujuan)
 
    for kombinasi in kombinasi:
        print(" ".join(str(x) for x in kombinasi))
 
 
if __name__ == "__main__":
    main()