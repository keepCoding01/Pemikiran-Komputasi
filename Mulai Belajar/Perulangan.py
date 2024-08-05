# Algoritma
# 1. Input angka
# 2. Inisialisasi list "angka" dengan panjang 10
# 3. Lakukan perulangan sebanyak inputan dan masukkan kedalam variabel simpan kemudian tambahkan satu ke elemen yang sesuai di dalam list angka, dengan mengubah tipe datanya ke integer
# 4. Lakukan perulangan kedua sebanyak "angka" kedalam variable jumlah dan cetak tiap elemen pada baris baru(kesamping)

masukan = input("Masukkan angka = ")

angka = [0] * 10

for simpan in masukan:
    angka[int(simpan)] += 1

for jumlah in angka:
    print(jumlah, end=" ")
