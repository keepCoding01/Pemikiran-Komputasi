# Algoritma
# 1. Mulai  
# 2. Masukkan deret kumpulan bilangan acak 
# 3. Lakukan perulangan sebanyak n untuk melakukan penjumlahan 
# 4. Hasil penjumlahan dibagi dengan n dan disimpan ke dalam variabel ratarata
# 5. Cetak ratarata 
# 6. Selesai

# Kompleksitas waktu = O(n)

bilangan = list(map(int,input("Masukkan deret bilangan: ").split()))
jumlah = 0
 
for i in range (len(bilangan)):
    jumlah += bilangan[i]
 
ratarata = jumlah / len(bilangan)
 
print("Rata-ratanya adalah %.2f"%ratarata)