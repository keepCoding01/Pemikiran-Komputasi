"""
1. Mulai
2. Input N
3. Lakukan perulangan untuk penjumlahan dan cetak deret
4. Hasil penjumlahan disimpan dalam variable jumlah 
5. Cetak hasil penjumlahan
6. Selesai
"""

n = int(input("Masukkan nilai : "))
jumlah = 0
for i in range(n+1):
    print(i, end = " ")
    jumlah += i
print()
print(jumlah)
