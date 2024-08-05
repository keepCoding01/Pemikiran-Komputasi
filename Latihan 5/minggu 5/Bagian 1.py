#Algoritma

# 1. Mulai
# 2. inisialisasi fungsi def fibo diisi dengan parameter n
# 3. Lakukan perkondisian :
#    - jika n == 1 atau n == 2, maka kembalikan nilai 1
#    - jika tidak, maka kembalikan nilai dari fungsi fibo dengan (n-1) ditambah (n-2)
# 4. inisialisasi fungsi def operasi diisi dengan parameter n
# 5. Buat variabel a dan b untuk menampung nilai 1 di indeks awal dan 1 di indeks kedua
# 6. Lakukan perulangan i sepanjang n, kemudian cetak fungsi fibo ke-i+1. lakukan ke indeks berikutnya
# 7. cetak fungsi operasi
# 8. selesai

# kompleksitas waktu = O(2n) + O(n)
 
n = int(input("Masukkan bilangan: "))
 
 
def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
 
 
def operasi(n):
    a, b = 1, 1
    for i in range(n):
        print(fibo(i+1), end=' ')
        a, b = b, a + b
    print()
 
 
operasi(n)


