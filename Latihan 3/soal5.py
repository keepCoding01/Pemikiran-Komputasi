# ALGORITMA
# 1. MULAI
# 2. BUAT FUNGSI DEF DFS DENGAN PARAMETER  s, i, dikunjungi, kelompok
# 3. SETIAP INDEKS dikunjungi = TRUE, TAMBAHKAN INDEKS KE VARIABEL KELOMPOK
# 4. LAKUKAN PERULANGAN nodeLain SELAMA INDEKS s :
#       JIKA INDEKS nodeLain TIDAK DIPAKAI :
#           BUAT FUNGSI DFS DENGAN PARAMETER s, nodeLain, dikunjungi, kelompok
# 5. BUAT FUNGSI DEF minKelompok DENGAN PARAMETER s, m
# 6. SET VARIABLE DIKUNJUNGI DENGAN NILAI FALSE * m
# 7. LAKUKAN PERULANGAN j SEPANJANG m
#       JIKA INDEKS DIKUNJUNGI TIDAK DIPAKAI, BERARTI VARIABLE KELOMPOK KOSONG NILAINYA
#       KEMUDIAN PANGGIL DEF DFS DAN TAMBAHKAN DATA KELOMPOK KE VAR KESELURUHAN
# 8. KEMBALIKAN NILAI VAR KESELURUHAN
# 9. BUAT DEF prosesGraph DENGAN PARAMETER m
# 10. INISIALISASI ARRAY KOSONG s
# 11. LAKUKAN PERULANGAN i SEPANJANG m
# 12. INPUT DATA PARA MANAGER DAN TAMBAHKAN DATANYA KE s, KEMUDIAN KEMBALIKAN
# 13. BUAT FUNGSI DEF MAIN
# 14. INPUT JUMLAH KARYAWAN
# 15. INISIALISASI FUNGSI DEF prosesGraph SEBAGAI s
# 16. INISIALISASI FUNGSI DEF minKelompok SEBAGAI VARIABLE KESELURUHAN
# 17. CETAK JUMLAH MINIMUM KELOMPOK
# 18. PANGGIL FUNGSI MAIN
# 19. SELESAI


# KOMPLEKSITAS WAKTU = O(n+e) ==> karena ini kasus terburuk. dimana DFS mengunjungi setiap node di grafik

# KOMPLEKSITAS RUANG = O(n) ==> karena DFS melakukan rekursif menggunakan stack dalam kedalaman hingga ke-n. dan ini adalah kasus terburuk


def dfs(s, i, dikunjungi, kelompok):
    dikunjungi[i] = True
    kelompok.append(i)
    for nodeLain in s[i]:
        if not dikunjungi[nodeLain]:
            dfs(s, nodeLain, dikunjungi, kelompok)


def minKelompok(s, m):
    dikunjungi = [False] * m
    keseluruhan = []
    for j in range(m):
        if not dikunjungi[j]:
            kelompok = []
            dfs(s, j, dikunjungi, kelompok)
            keseluruhan.append(kelompok)
    return len(keseluruhan)


def prosesGraph(m):
    s = []
    for i in range(m):
        paraManager = [int(x) for x in input(
            f"Masukkan manajer karyawan {i+1}: ").split()]
        s.append(paraManager)
    return s


def main():
    m = int(input("Jumlah karyawan: "))
    s = prosesGraph(m)
    keseluruhan = minKelompok(s, m)
    print(f"Jumlah minimum kelompok di pesta : {keseluruhan-1}")


main()
