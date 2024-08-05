# ALGORITMA

# 1. INISIALISASI FUNGSI DEF MERGESORT DENGAN PARAMETER ARRAY
# 	- JIKA PANJANG ARRAY > 1, SET VAR TENGAH, KIRI DAN KANAN
# 	- PANGGIL MERGESORT KIRI DAN KANAN
# 	- INISIALISASI I = J = K = 0
# 	- LAKUKAN PERULANGAN SELAMA I < PANJANG KIRI DAN J < PANJANG KANAN
# 	- JIKA KIRI < KANAN, INDEKS K ARRAY = INDEKS I KIRI, TAMBAHKAN I DENGAN 1
# 	- JIKA TIDAK, INDEKS K ARRAY = INDEKS J KANAN, J + 1, K + 1
# 	- SELAMA I < KIRI, INDEKS K ARRAY = INDEKS I KIRI, I + 1, K + 1
# 	- SELAMA J < KANAN, INDEKS K ARRAY = INDEKS J KANAN, J + 1, K + 1
# 2. INISIALISASI FUNGSI DEF MEMBUATGRAPH DENGAN PARAMETER N
# 	- INISIALISASI VARIABEL GRAPH DENGAN DICT KOSONG
# 	- LAKUKAN PERULANGAN SELAMA N
# 	- INPUT NILAI RUMAH DAN TETANGGA
# 	- JIKA PANJANG TETANGGA > 1, PANGGIL FUNGSI MERGESORT DENGAN PARAMETER TETANGGA
# 	- MASUKKAN TETANGGA MENJADI INDEKS RUMAH PADA GRAPH
# 	- KEMBALIKAN NILAINYA
# 3. INISIALISASI FUNGSI DEF JALURBFS DENGAN PARAMETER GRAPH DAN START
# 	- SET VARIABEL TELAH DIKUNJUNGI
# 	- INISIALISASI QUEUE DENGAN LIST START
# 	- INISIALISASI JALUR DENGAN LIST KOSONG
# 	- LAKUKAN PERULANGAN QUEUE
# 	- LAKUKAN PENGHAPUSAN NILAI QUEUE DI BELAKANG DAN MASUKKAN KE VARIABEL NODE
# 	- JIKA NOT BUKAN VARIABEL TELAHDIKUNJUNGI, MAKA TAMBAHKAN NODE KE VARIABEL TELAHDIKUNJUNGI DAN JALUR
# 	- JIKA NODE ADA DI GRAPH, INDEKS NODE PADA GRAPH MASUKKAN KE VARIABEL SELURUHTETANGGA.
# 	- LAKUKAN PERULANGAN SELAMA TETANGGA ADA DI VARIABEL SELURUHTETANGGA, DAN JIKA BUKAN YANG TELAHDIKUNJUNGI MAKA TAMBAHKAN NILAINYA KE VARIABEL QUEUE
# 	- KEMBALIKAN NILAINYA
# 4. INPUT NILAI JUMLAHRUMAH DAN RUMAHPERTAMA
# 5. PANGGIL FUNGSI MEMBUATGRAPH -> SIMPAN KE VARIABEL GRAPH + PANGGIL FUNGSI JALURBFS -> SIMPAN KE VARIABEL JALUR
# 6. CETAK NILAI YANG ADA DI VARIABEL JALUR DENGAN JOIN

# KOMPLEKSITAS WAKTU : O (N LOG N) + O (V + E)
# KOMPLEKSITAS RUANG : O (N + V)

def mergeSort(array):
    if len(array) > 1:
        tengah = len(array) // 2
        kiri = array[:tengah]
        kanan = array[tengah:]

        mergeSort(kiri)
        mergeSort(kanan)

        i = j = k = 0
        while i < len(kiri) and j < len(kanan):
            if kiri[i] < kanan[j]:
                array[k] = kiri[i]
                i += 1
            else:
                array[k] = kanan[j]
                j += 1
            k += 1

        while i < len(kiri):
            array[k] = kiri[i]
            i += 1
            k += 1

        while j < len(kanan):
            array[k] = kanan[j]
            j += 1
            k += 1


def membuatGraph(N):
    graph = {}
    for _ in range(N):
        rumah = input().strip()
        tetangga = input().strip().split()
        if len(tetangga) > 1:
            mergeSort(tetangga)
        graph[rumah] = tetangga
    return graph


def jalurBFS(graph, start):
    telahDikunjungi = set()
    queue = [start]
    jalur = []

    while queue:
        node = queue.pop(0)
        if node not in telahDikunjungi:
            telahDikunjungi.add(node)
            jalur.append(node)
            if node in graph:
                seluruhTetangga = graph[node]
                for tetangga in seluruhTetangga:
                    if tetangga not in telahDikunjungi:
                        queue.append(tetangga)
    return jalur


jumlahRumah = int(input().strip())

graph = membuatGraph(jumlahRumah)

rumahPertama = input().strip()

jalur = jalurBFS(graph, rumahPertama)

print(" -> ".join(jalur))
