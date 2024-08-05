# ALGORITMA
# inisialisasi fungsi cariCEO dengan parameter n dan matriks
# inisialisasi variabel telahDikunjungi dengan panjang n
# inisialisasi fungsi bfs dengan parameter start
# cek apakah semua simpul telah dikunjungi dengan nilai True
# jika belum dikunjungi, lakukan perulangan untuk mencari simpul sepanjang n
# jika semua telah dikunjungi maka cetak semua komputer terhubung
# jika tidak, maka cetak yang belum dikunjungi sebagai komputer CEO
# inialisasi fungsi main
# inisialisasi matriks dengan list kosong
# lakukan perulangan sepanjang n dan input nilai matriks, input nilai baris dan kolom
# panggil fungsi main, kemudian simpan di variabel matriks
# panggil fungsi cariCEO, kemudian simpan ke variable output
# cetak output


# Kompleksitas = Big O(n^2)

def cariCEO(n, matriks):
    telahDikunjungi = [False] * n

    def bfs(start):
        telusuri = [start]
        telahDikunjungi[start] = True
        while telusuri:
            node = telusuri.pop(0)
            for i in range(n):
                if matriks[node][i] == 1 and not telahDikunjungi[i]:
                    telusuri.append(i)
                    telahDikunjungi[i] = True

    bfs(0)

    if all(telahDikunjungi):
        return "Semua komputer terhubung"
    else:
        for i in range(n):
            if not telahDikunjungi[i]:
                return f"Komputer {i+1} adalah komputer CEO"


def main(n):
    matriks = []
    for _ in range(n):
        barisMatriks = list(map(int, input().split()))
        matriks.append(barisMatriks)
    return matriks


n = int(input())
matriks = main(n)


output = cariCEO(n, matriks)
print(output)
