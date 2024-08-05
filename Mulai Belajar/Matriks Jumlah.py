n = int(input("Masukkan jumlah baris dan kolom matrix : "))
print("Matriks 1")
matrix1 = []
for i in range(n):
    baris = []
    for j in range(n):
        baris.append(int(input(f"Masukkan elemen matrix 1 [{i+1}][{j+1}] : ")))
    matrix1.append(baris)

print("Matriks 2")
matrix2 = []
for i in range(n):
    baris = []
    for j in range(n):
        baris.append(int(input(f"Masukkan elemen matrix 2 [{i+1}][{j+1}] : ")))
    matrix2.append(baris)

print("hasil matrix :")
hasilPenjumlahan = []
for i in range(n):
    hasilPenjumlahan.append([])
    for j in range(n):
        hasilPenjumlahan[i].append(matrix1[i][j] + matrix2[i][j])

print("Matriks 1:")
for baris in matrix1:
    print(baris)

print("Matriks 2:")
for baris in matrix2:
    print(baris)

print("Hasil Penjumlahan:")
for baris in hasilPenjumlahan:
    print(baris)
