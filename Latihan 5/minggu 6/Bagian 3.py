 
# 1. Mulai
# 2. Buat fungsi MergeSort dengan parameter x dan n.
# 3. Jika n kurang dari atau sama dengan 1, kembalikan hasil x pangkat n.
# 4. Bagi n menjadi dua bagian.
# 5. Lakukan MergeSort secara iteratif untuk setengah bagian pertama x dan setengah bagian kedua x.
# 6. Kalikan hasil kedua bagian dalam rekursi tersebut.
# 7. Kembalikan hasil perkalian bagian pertama dan kedua.
# 8. Input bilangan real dan pangkat.
# 9. Hitung hasil dengan fungsi MergeSort.
# 10. Cetak hasil
# 11. Selesai

def MergeSort(x, n):
    if n <= 1:
        return x ** n
 
    bagiDuaBagian = n // 2
    bagianPertama = MergeSort(x, bagiDuaBagian)
    bagianKedua = MergeSort(x, n - bagiDuaBagian)
    
    hasil = bagianPertama * bagianKedua
    print(hasil)
    return hasil
    
 
 
x = int(input("Masukkan bilangan real: "))
n = int(input("Masukkan pangkat: "))
hasil = MergeSort(x, n)
 
print(f"Hasil {x} pangkat {n} adalah {hasil}")
