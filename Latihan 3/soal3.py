# ALGORITMA
# 1. MULAI
# 2. INPUT NILAI X DAN Y
# 3. INISIALISASI VARIABEL JUMLAH DENGAN NILAI 0
# 4. LAKUKAN PERULANGAN i MULAI DARI X SAMPAI Y + 1
# 5. INISIALISASI VARIABEL FAKTOR DENGAN NILAI 0
# 6. LAKUKAN PERULANGAN j MULAI DARI 1 SAMPAI i + 1
# 7. JIKA i mod j SAMA DENGAN 0, MAKA FAKTOR DITAMBAH 1
# 8. JIKA FAKTOR LEBIH DARI 2, MAKA JUMLAH DITAMBAH 1
# 9. CETAK JUMLAH BILANGAN KOMPOSIT
# 10. SELESAI

# KOMPLEKSITAS = O(n^2)
# KOMPLEKSITAS WAKTU = O(1)

x, y = map(int, input(
    "Nilai batas x dan y, dipisahkan oleh sebuah spasi = ").split())

jumlah = 0

for i in range(x, y + 1):
    faktor = 0
    for j in range(1, i + 1):
        if i % j == 0:
            faktor += 1

    if faktor > 2:
        jumlah += 1

print(f"Jumlah bilangan komposit : {jumlah}")
