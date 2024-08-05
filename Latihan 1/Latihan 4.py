# ALGORITMA
# inisialisasi fungsi cekSiklis dengan parameter petaGame
# inisialisasi variabel m,n dengan nilai dari masing-masing panjang petaGame
# inisialisasi variabel telahDikunjungi untuk membuat matriks
# inisialisasi variabel valid dengan parameter baris dan kolom
# kembalikan nilai baris dalam rentang 0 hingga m dan kolom dalam rentang 0 hingga n dan baris kolom dari petaGame apakah ia merupakan . ( karakter titik)
# lakukan perulangan barisAwal sepanjang m, lakukan perulangan kolomAwal sepanjang n
# jika petaGame == . dan bukan yang sudah dikunjungi, maka masukkan nilainya kedalam antrian
# selama antrian, baris sekarang, kolomSekarang, barisSebelum, kolomSebelum akan dilakukan penghapusan pada indeks ke 0
# jika telah dikunjungi, kembalikan YES dan tukar nilainya menjadi TRUE
# lakukan perulangan melalui empat kemungkinan (atas,bawah,kiri,kanan)
# hitung koordinat baris dan kolom berdasarkan perubahan dari posisi sekarang
# perikasa apakah posisi tetangga valid atau tidak, tambahkan yang valid ke dalam antrian dan jika tidak ditemukan jalur yang memutar cetak NO
# inisialisasi fungsi main
# input nilai m, n dan peta gamenya
# panggil fungsi main dan simpan ke dalam variabel petaGame
# panggil fungsi cekSiklis dan simpan nilainya ke dalam variabel output
# cetak output


# Kompleksitas = Big O(1) + Big O(m*n)


def cekSiklis(petaGame):
    m, n = len(petaGame), len(petaGame[0])
    telahDikunjungi = [[False] * n for _ in range(m)]

    def valid(baris, kolom):
        return 0 <= baris < m and 0 <= kolom < n and petaGame[baris][kolom] == '.'

    for barisAwal in range(m):
        for kolomAwal in range(n):
            if petaGame[barisAwal][kolomAwal] == '.' and not telahDikunjungi[barisAwal][kolomAwal]:
                antrian = [(barisAwal, kolomAwal, -1, -1)]
                while antrian:
                    barisSekarang, kolomSekarang, barisSebelum, kolomSebelum = antrian.pop(
                        0)
                    if telahDikunjungi[barisSekarang][kolomSekarang]:
                        return "YES"
                    telahDikunjungi[barisSekarang][kolomSekarang] = True
                    # atas, bawah, kiri, kanan
                    for perubahanBaris, perubahanKolom in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        barisTetangga, kolomTetangga = barisSekarang + \
                            perubahanBaris, kolomSekarang + perubahanKolom
                        if valid(barisTetangga, kolomTetangga) and (barisTetangga, kolomTetangga) != (barisSebelum, kolomSebelum):
                            antrian.append(
                                (barisTetangga, kolomTetangga, barisSekarang, kolomSekarang))
    return "NO"


def main():
    m, n = map(int, input().strip().split())
    petaGame_input = []
    for _ in range(m):
        baris = list(input().strip())
        petaGame_input.append(baris)
    return petaGame_input


petaGame = main()

output = cekSiklis(petaGame)
print(output)
