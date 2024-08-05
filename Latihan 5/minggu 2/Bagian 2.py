"""
Algoritma :


"""


n = int(input("Masukkan jumlah matrix : "))
print("Matriks 1")
matrix1 = []
for i in range(n):
    baris = []
    for j in range(n):
        baris.append(n)
    matrix1.append(baris)
    print(baris)

n = int(input("Masukkan jumlah matrix : "))
print("Matriks 2")
matrix2 = []
for f in range(n):
    baris = []
    for g in range(n):
        baris.append(n)
    matrix2.append(baris)
    print(baris)

matrix_hasil = []
for i in range(n):
    for j in range(n):
        matrix_hasil[i][j] = matrix1[i][j] + matrix2[i][j]
print("Matriks Hasil")
print(matrix_hasil)


matrix = []
print("Matriks Hasil")
jumlahbaris = [i] + [i]
jumlahkolom = [j] + [j]
for i in range(n):
    matrix.append(jumlahbaris)
    for j in range(n):
        baris.append(jumlahkolom)
        print(baris)
    print(matrix)




