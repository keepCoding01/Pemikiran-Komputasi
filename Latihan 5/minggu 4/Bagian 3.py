#ALGORITMA
# Mulai
# Membaca input dari user
# Inisialisasi variabel bilangan prima
# Melakukan complete search terhadap setiap bilangan
    # Jika bilangan lebih dari 1 (karena hanya bilangan lebih dari 1 yang bisa prima)
    # Inisialisasi variabel prima
    # Melakukan complete search terhadap setiap bilangan kurang dari sama dengan bilangan sqrt(i)
    # Jika i habis dibagi j, maka i tidak prima
    # Selesai mencari, exit dari perulangan
    # Jika i prima
    # Tambahkan 1 ke bilangan prima
# Tampilkan jumlah bilangan prima
# Selesai

bilangan = list(map(int, input().split()))
jumlah = 0
for i in bilangan:
    if i > 1:
        prima = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                prima = False
                break
        if prima:
            jumlah += 1
 
print(jumlah)