# ALGORITMA
# 1. BUAT FUNGSI TOWER OF HONEI
# 2. INISIALISASI 3 RAK SEBAGAI TEMPAT PERPINDAHAN DISKNYA NANTI
# 3. CETAK BUKU 1 PINDAH DARI RAK A KE B
# 4. PINDAHKAN BUKU PALING ATAS DARI RAK A KE RAK BaseException
# 5. BUAT PERULANGAN SELAMA i < JUMLAH BUKU + 1:
#     - JIKA JUMLAH BUKU GENAP:
#         CETAK BUKU i PINDAH DARI RAK A KE C
#     - JIKA JUMLAH BUKU GANJIL:
#         CETAK BUKU i PINDAH DARI RAK A KE B
#         PINDAHKAN BUKU PALING ATAS DARI RAK A KE RAK B
#         CETAK BUKU 1 PINDAH DARI RAK B KE C
#         POINDAHKAN BUKU PALING ATAS DARI RAK B KE C
# 6. BUAT PERULANGAN WHILE UNTUK RAK B:
#     CETAK BUKU 1 PINDAH DARI RAK B KE C
#     PINDAHKAN BUKU PALING ATAS DARI RAK B KE C
# 7. INPUT JUMLAH BUKU
# 8. PANGGIL FUNGSI TOWER OF HANOI
# 8. SELESAI

def TowerOfHanoi(n):
    rakA = list(range(1, n + 1))
    rakB = []
    rakC = []

    print(f"Buku 1 pindah dari RAK A ke B")
    rakB.append(rakA.pop(0))

    for i in range(2, n + 1):
        if i % 2 == 0:
            print(f"Buku {i} pindah dari Rak A ke C")

            rakC.append(rakA.pop(0))
        else:
            print(f"Buku {i} pindah dari Rak A ke B")

            rakB.append(rakA.pop(0))
            print(f"Buku 1 pindah dari Rak B ke C")

            rakC.append(rakB.pop(0))

    while rakB:
        print(f"Buku 1 pindah dari Rak B ke C")
        rakC.append(rakB.pop(0))


n = int(input("Masukkan jumlah buku : "))
TowerOfHanoi(n)
