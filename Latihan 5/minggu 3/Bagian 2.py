# Algoritma
# 1. Mulai
# 2. Input angka
# 3. Inisialisasi list "angka" dengan panjang 10 dan masing-masing bernilai 0
# 4. Lakukan perulangan sebanyak inputan dan masukkan kedalam variabel simpan kemudian tambahkan satu ke elemen yang sesuai di dalam list angka, dengan mengubah tipe datanya ke integer
# 5. Lakukan perulangan kedua sebanyak "angka" kedalam variable jumlah dan cetak tiap elemen pada baris baru(kesamping)
# 6. Selesai
 
# Kompleksitas waktu = O(n) + O(n)

masukan = list(map(int,input("Masukkan deret bilangan: ").split()))
 
angka = [0,0,0,0,0,0,0,0,0,0]
 
for simpan in masukan:
    angka[int(simpan)] += 1
 
for jumlah in angka:
    print(jumlah, end=" ")