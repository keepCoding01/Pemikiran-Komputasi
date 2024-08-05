def cariKombinasi(angka, tujuan):
    hasil = []
 
    def nodeKembali(kombinasi, sisa, mulai):
        if sisa == 0:
            hasil.append(kombinasi[:])
            return
        for i in range(mulai, len(angka)):
            if angka[i] > sisa:
                break
            kombinasi_temp = kombinasi[:]
            kombinasi_temp.append(angka[i])
            nodeKembali(kombinasi_temp, sisa - angka[i], i)
 
    nodeKembali([], tujuan, 0)
    return hasil
 
def main():
    angka = [int(x) for x in input("Masukkan bilangan acak: ").split()]
    tujuan = int(input("Masukkan bilangan yang ingin dicari kombinasi penjumlahannya: "))
    kombinasi = cariKombinasi(angka, tujuan)
    print("Semua kemungkinan penjumlahahan:")
    for kombinasi in kombinasi:
        print(" ".join(str(x) for x in kombinasi))
 
if __name__ == "__main__":
    main()
