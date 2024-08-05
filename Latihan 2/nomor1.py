# ALGORITMA

# 1. INISIALISASI FUNGSI DEF DJIKSTRA DENGAN PARAMETER JLHVERTEX, GRAPH, SIMPUL ASAL.
# 	- INISIALISASI VARIABEL NILAITAKHINGGA DENGAN FLOAT INF
# 	- INISIALISASI VARIABEL JARAK DENGAN MENGALIKAN LIST DARI NILAITAKHINGGA DENGAN JLHVERTEX
# 	- INISIALISASI VARIABEL TELAHDIKUNJUNGI DENGAN MENGALIKAN NILAI FALSE PADA JLHVERTEX
# 	- INISIALISASI INDEX SIMPULASAL PADA VARIABEL JARAK DENGAN 0
# 	- LAKUKAN PERULANGAN SELAMA JLHVERTEX, APABILA JARAKMINIMAL SAMA DENGAN NILAITAKHINGGA, INISIALISASI VARIABEL U = -1
# 	- LAKUKAN PERULANGAN V SELAMA JLHVERTEX, JIKA BUKAN INDEKS V TELAH DIKUNJUNGI DAN JARAK < JARAK MINIMAL, LAKUKAN PERTUKARAN DATA DAN INISIALISASI DENGAN U = V.
# 	- UBAH INDEKS U TELAHDIKUNJUNGI DENGAN NILAI TRUE.
# 	- LAKUKAN PERULANGAN V SELAMA JLHVERTEX, JIKA INDEKS DARI U DAN V PADA GRAPH BUKAN INDEKS V PADA VARIABEL TELAHDIKUNJUNGI DAN INDEKSU PADA VARIABEL JARAK + INDEKS U V PADA GRAPH < INDEKS V PADA JARAK, MAKA INDEKS U PADA JARAK DITAMBAH INDEKS U DAN V PADA GRAPH KEMUDIAN MASUKKAN KE INDEKS V PADA JARAK.
# 	- KEMBALIKAN NILAINYA.
# 2. INISIALISASI FUNGSI DEF SHORTESTPATHDJIKSTRA DENGAN PARAMETER JLHVERTEX, SISI, AWAL, AKHIR.
# 	- BERIKAN NILAI INF PADA VARIBEL NILAITAKHINGGA
# 	- LAKUKAN PERKALIAN NILAITAKHINGGA DENGAN JLHVERTEX SELAMA PERULANGAN JLHVERTEX DIDALAM VARIABEL GRAPH
# 	- LAKUKAN PERULANGAN U,V,W PADA VARIABEL SISI
# 	PANGGIL FUNGSI DIJKSTRA DENGAN INDEKS AKHIR-1 DAN MASUKKAN KEDALAM VARIABEL JARAKPALINGPENDEK
# 	- INISIALISASI VARIABEL SEMUAJALUR DENGAN LIST KOSONG
# 3. INISIALISASI FUNGSI DFS DIDALAM FUNGSI DEF SHORTESTPATHDJIKSTRA DENGAN PARAMETER NODESEKARANG, JARAKSEKARANG, JALUR.
# 	- JIKA JARAKSEKARANG > JARAKPALINGPENDEK, KEMBALIKAN NILAINYA.
# 	- JIKA NODESEKARANG == AKHIR-1, MAKA COPY JALUR DAN TAMBAHKAN KE VARIABEL SEMUAJALUR KEMUDIAN KEMBALIKAN NILANYA
# 	- LAKUKAN PERULANGAN TETANGGA DENGAN JLHVERTEX, JIKA INDEKS GRAPH TIDAK SAMA DENGAN NILAITAKHINGGA DAN TETANGGA TIDAK DIJALUR, MAKA TAMBAHKAN TETANGGA KEDALAM VARIABEL JALUR KEMUDIAN PANGGIL FUNGSI DEF. HAPUS NILAI JALUR DARI BELAKANG
# 	- INISIALISASI VARIABEL JUMLAH DENGAN LIST YANG BERISI 0, KEMUDIAN KALIKAN DENGAN JLHVERTEX
# 	- LAKUKAN PERULANGAN UNTUK JALUR SELAMA SEMUAJALUR, LAKUKAN PERULANGAN NODE DIDALAM JALUR, KEMUDIAN TAMBAH 1 TIAP INDEKS NODE PADA JALUR
# 4. INPUT NILAI DAN PANGGIL FUNGSI SHORTESTPATHDJIKSTRA KEMUDIAN LAKUKAN PERULANGAN UNTUK SETIAP NILAI HASILAKHIR DI HASIL.
# 5. CETAK HASILAKHIR

# KOMPLEKSITAS WAKTU  : O(2^N)
# KOMPLEKSITAS RUANG   : O(N^2) +  O(N)

def dijkstra(jlhVertex, graph, simpulAsal):
    nilaiTakHingga = float('inf')
    jarak = [nilaiTakHingga] * jlhVertex
    telahDikunjungi = [False] * jlhVertex
    jarak[simpulAsal] = 0

    for _ in range(jlhVertex):
        jarakMinimal = nilaiTakHingga
        u = -1
        for v in range(jlhVertex):
            if not telahDikunjungi[v] and jarak[v] < jarakMinimal:
                jarakMinimal = jarak[v]
                u = v
        telahDikunjungi[u] = True

        for v in range(jlhVertex):
            if graph[u][v] and not telahDikunjungi[v] and jarak[u] + graph[u][v] < jarak[v]:
                jarak[v] = jarak[u] + graph[u][v]

    return jarak


def shortestPathDjikstra(jlhVertex, sisi, awal, akhir):
    nilaiTakHingga = float('inf')
    graph = [[nilaiTakHingga] * jlhVertex for _ in range(jlhVertex)]
    for u, v, w in sisi:
        graph[u-1][v-1] = w
        graph[v-1][u-1] = w

    jarakPalingPendek = dijkstra(jlhVertex, graph, awal-1)[akhir-1]

    semuaJalur = []

    def dfs(nodeSekarang, jarakSekarang, jalur):
        if jarakSekarang > jarakPalingPendek:
            return
        if nodeSekarang == akhir-1:
            semuaJalur.append(jalur.copy())
            return
        for tetangga in range(jlhVertex):
            if graph[nodeSekarang][tetangga] != nilaiTakHingga and tetangga not in jalur:
                jalur.append(tetangga)
                dfs(tetangga, jarakSekarang +
                    graph[nodeSekarang][tetangga], jalur)
                jalur.pop()

    dfs(awal-1, 0, [awal-1])

    jumlah = [0] * jlhVertex
    for jalur in semuaJalur:
        for node in jalur:
            jumlah[node] += 1

    ratarataKunjungan = [int(t * 2 / len(semuaJalur)) for t in jumlah]
    return ratarataKunjungan


jlhVertex, jlhSisi, awal, akhir = map(int, input().split())
sisi = [tuple(map(int, input().split())) for _ in range(jlhSisi)]
hasil = shortestPathDjikstra(jlhVertex, sisi, awal, akhir)
for hasilakhir in hasil:
    print(hasilakhir)
