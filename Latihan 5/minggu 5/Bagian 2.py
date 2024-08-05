# ALGORITMA
# 1. Mulai
# 2. Input nilai
# 3. Inisialisasi fungsi def konversi dengan parameter n
# 4. Lakukan pengkondisian :
#     - Jika n == 0, maka kembalikan nilai 0
#     - Jika n == 1, maka kembalikan nilai 1
#     - Jika tidak keduanya, maka kembalikan nilai dari fungsi konversi dengan 
#       membagikan nilai n dengan 2 dan jumlahkan dengan hasil n mod 2
# 5. Inisialisasi variabel tempatBinary untuk menampung bilangan dari fungsi konversi
# 6. Cetak hasil yang ada di variable tempatBinary
# 7. Selesai
 
# kompleksitas waktu = O(n)
 
n = int(input("Masukkan bilangan : "))
 
 
def konversi(n):
    if n == 0:
        return '0'
    elif n == 1:
        return '1'
    else:
        return konversi(n // 2) + str(n % 2)
 
 
tempatBinary = konversi(n)
print(tempatBinary)
