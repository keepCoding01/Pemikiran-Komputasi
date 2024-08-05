# ALGORITMA
# 1. input nilai
# 2. buat fungsi def fibonacci
# 3. lakukan pengkondisian :
#    a. jika n == 1 atau n == 2, kembalikan nilai 1
#    b. jika tidak, kembalikan nilai fibonacci dengan mengurangkan n dengan 1
#       kemudian jumlahkan fibonacci dengan n-2
# 4. buat fungsi generate
# 5. inisialisasi variabe a dan b untuk menyimpan dua nilai yang akan dijumlahkan
# 6. lakukan perulangan i selama n
# 7. cetak fibonacci yang sudah dijumlahkan
# 8. lakukan penjumlahan kembali dari angka sebelumnya
# 9. cetak perulangan dan lakukan pemanggilan fungsi generatenya

# kompleksitas waktu = O(n) + O(n)

n = int(input("Masukkan jumlah bilangan Fibonacci yang ingin ditampilkan: "))


def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def generate(n):
    a, b = 1, 1
    for i in range(n):
        print(fibonacci(i+1), end=' ')
        a, b = b, a + b
    print()


generate(n)
