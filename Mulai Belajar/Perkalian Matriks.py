# Algoritma
# 1. Input n untuk memasukkan jumlah baris dan kolom
# 2. Print "Matriks 1"
# 3. Inisialisasi array kosong matrix1
# 4. Lakukan perulangan i sepanjang n
# 5. Inisialisasi array kosong baris
# 6. Lakukan perulangan j didalam perulangan i sepanjang n
# 7. Input tiap elemen dan tambahkan ke variabel baris
# 8. Tambahkan elemen baris ke matrix1
# 9. Print "Matriks 2"
# 10. Inisialisasi array kosong matrix2
# 11. Lakukan perulangan i sepanjang n
# 12. Inisialisasi array kosong baris
# 13. Lakukan perulangan j didalam perulangan i sepanjang n
# 14. Input tiap elemen dan tambahkan ke variabel baris
# 15. Tambahkan elemen baris ke matrix2
# 16. Print hasil perkalian
# 17. Inisialisasi array kosong hasilPerkalian
# 18. Lakukan perulangan i sepanjang n
# 19. Untuk setiap baris, buat list baru dan tambahkan ke dalam hasilPerkalian
# 20. Lakukan perulangan j didalam perulangan i sepanjang n
# 21. Untuk setiap kolom, hitung hasil perkalian dari setiap baris dan kolom pada matriks 1 dan matriks 2, dan simpan hasilnya ke dalam hasilPerkalian.
# 22. Print Matriks 1
# 23. Lakukan perulangan baris didalam matrix1
# 24. Print baris
# 25. Print Matriks 2
# 26. Lakukan perulangan baris di matrix2
# 27. Print baris
# 28. Print Hasil Perkalian 
# 29. Lakukan perulangan baris didalam hasilPerkalian
# 30. Print baris


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

print("hasil perkalian :")
hasilPerkalian = []
for i in range(n):
    hasilPerkalian.append([])
    for j in range(n):
        hasilPerkalian[i].append(
            sum(matrix1[i][k] * matrix2[k][j] for k in range(n)))

print("Matriks 1:")
for baris in matrix1:
    print(baris)

print("Matriks 2:")
for baris in matrix2:
    print(baris)

print("Hasil Perkalian:")
for baris in hasilPerkalian:
    print(baris)

