#ALGORITMA
# Mulai
# Membaca input dari user
# Melakukan complete search terhadap setiap karakter pada string pattern
# Jika semua karakter pada string pattern ditemukan pada string teks
    # Maka kata pattern ditemukan pada string teks
    # Selesai mencari, exit dari perulangan
    # print 'Ketemu'
# Jika tidak ditemukan, maka tampilkan 'Tidak ketemu'
# Selesai

pattern = input("String pattern: ")
teks = input("String teks: ")
cari = False
for i in range(len(teks) - len(pattern) + 1):
    if(teks[i:i+len(pattern)] == pattern):
        print("Ketemu")
        cari = True
        break
if not cari:
    print("Tidak Ketemu")