# ALGORITMA
# 1. input bilangan
# 2. buat fungsi def untuk melakukan pemanggilan konversi binary, sepanjang inputan (n)
# 3. a. jika n == 0, kembalikan string 0
#    b. jika n == 1, kembalikan string 1
#    c. jika tidak keduanya, kembalikan hasil konversi binary dengan membagi n dengan 2
#       ditambah string n mod 2
# 4. inisialisasi variable binary untuk menampung konversiBinary
# 5. cetak bilangan

# kompleksitas waktu = O(n)

n = int(input("Masukkan bilangan desimal: "))


def konversiBinary(n):
    if n == 0:
        return '0'
    elif n == 1:
        return '1'
    else:
        return konversiBinary(n // 2) + str(n % 2)


binary = konversiBinary(n)
print(f"Bilangan biner dari {n} adalah: {binary}")
