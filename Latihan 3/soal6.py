# ALGORITMA
# 1. MULAI
# 2. INPUT NILAI N DAN HOME
# 3. BUAT FUNGSI DEF MERGESORT DENGAN PARAMETER HOME
# 4. JIKA SEPANJANG HOME NILAINYA KURANG DARI 1, MAKA KEMBALIKAN NILAINYA
# 5. INISIALISASI VARIABLE MID DENGAN NILAINYA SEPANJANG HOME
# 6. INISIALISASI VARIABLE LEFT DAN RIGHT DENGAN MENGGUNAKAN FUNGSI DEF MERGESORT
# 7. KEMBALIKAN NILAI MERGE DARI LEFT DAN RIGHT
# 8. BUAT FUNGSI DEF MERGE DENGAN PARAMETER LEFT DAN RIGHT
# 9. INISIALISASI VARIABLE I DAN J = 0 DAN ARRAY KOSONG HASIL
# 10. LAKUKAN PERULANGAN SELAMA I < PANJANG LEFT DAN J < PANJANG RIGHT
# 11. JIKA INDEKS LEFT I < INDEKS RIGHT J, INDEKS LEFT I DITAMBAHKAN KE VARIABLE HASIL
# 12. JIKA TIDAK, TAMBAHKAN INDEKS RIGHT J KE VARIABLE HASIL
# 13. TAMBAHKAN INDEKS LEFT I DAN RIGHT J KE VARIABLE HASIL, KEMUDIAN KEMBALIKAN NILAINYA
# 14. BUAT FUNGSI DEF GAME DENGAN PARAMETER HOME
# 15. MASUKKAN NILAI YANG ADA DIHOME KE VARIABLE N
# 16. INISIALISASI VARIABLE URUTAN DAN MASUKKAN NILAI DARI MERGESORT YANG PARAMETERNYA HOME
# 17. INISIALISASI VARIABLE SISA DAN MASUKKAN NILAI N KE DALAMNYA
# 18. LAKUKAN PERULANGAN KETIKA SISA > 1, URUTAN INDEKS KE 0 DIMASUKKAN KE VARIABLE MINNILAI
# 19. INISIALISASI MININDEKS = 0
# 20. LAKUKAN PERULANGAN I SELAMA N, JIKA INDEKS HOME == MINNILAI, MININDEKS = I DAN LAKUKAN PENGHENTIAN
# 21. SET HOME INDEKS KE MININDEKS = -1
# 22. KURANGKAN VARIABLE SISA DENGAN 1
# 23. INDEKS -1 VARIABLE URUTAN DIMASUKKAN KE DALAM VARIABLE MAXNILAI
# 24. INISIALISASI VARIABLE MAXINDEKS = 0
# 25. LAKUKAN PERULANGAN I SELAMA N, JIKA INDEKS HOME == MAXNILAI MAKA MAXINDEKS = I DAN LAKUKAN PENGHENTIAN
# 26. SET INDEKS HOME DARI MAXINDEKS = -1
# 27. KURANGKAN SISA DENGAN 1
# 28. LAKUKAN PERULANGAN I SELAMA N, JIKA INDEKS HOME TIDAK SAMA DENGAN -1 MAKA KEMBALIKAN NILAINYA
# 29. INISIALISASI VARIABLE HASIL DAN MASUKKAN NILAI DARI FUNGSI GAME DENGAN PARAMETER HOME
# 30. CETAK SATU ANGKA YANG TERSISA DI PAPAN YAITU ... HASILNYA
# 31. SELESAI

# KOMPLEKSITAS = O(n log n)


n = int(input("Jumlah angka : "))
home = [int(input(f"Masukkan angka ke-{x+1} : ")) for x in range(n)]


def mergeSort(home):
    if len(home) <= 1:
        return home

    mid = len(home) // 2
    left = mergeSort(home[:mid])
    right = mergeSort(home[mid:])

    return merge(left, right)


def merge(left, right):
    i = 0
    j = 0
    hasil = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            hasil.append(left[i])
            i += 1
        else:
            hasil.append(right[j])
            j += 1

    hasil += left[i:]
    hasil += right[j:]
    return hasil


def game(home):
    n = len(home)

    urutan = mergeSort(home)

    sisa = n
    while sisa > 1:
        minNilai = urutan[0]

        minIndeks = 0
        for i in range(n):
            if home[i] == minNilai:
                minIndeks = i
                break

        home[minIndeks] = -1

        sisa -= 1

        maxNilai = urutan[-1]
        maxIndeks = 0
        for i in range(n):
            if home[i] == maxNilai:
                maxIndeks = i
                break

        home[maxIndeks] = -1

        sisa -= 1

    for i in range(n):
        if home[i] != -1:
            return home[i]


hasil = game(home)

print("Satu angka yang tersisa di papan yaitu : ", hasil)
