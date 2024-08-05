#ALGORITMA 
# 1. Mulai
# 2. Lakukan perulangan konversi dengan parameter angka dan hasil
# 3. Selama angka masih kurang dari 9, lakukan perkondisian
# 4. cetak hasil 
# 5. Jika angka bukan dari < 8, lakukan pembagian angka/8
# 6. Panggil fungsi konversi dan masukkan temp1 dan hasil sebagai parameternya
# 7. Angka dimodulo dengan 8 dan simpan dalam variabel temp2
# 8. Panggil fungsi konversi dengan parameter temp2 dan hasil
# 9. Inisialisasi variabel hasil dengan string
# 10. Lakukan konversi
# 11. Selesai

def konversi (angka, hasil):
    if angka < 8 :
        if angka == 0:
            hasil += "000"
        elif angka == 1:
            hasil += "001"
        elif angka == 2 :
            hasil += "010"
        elif angka == 3:
            hasil += "011"
        elif angka == 4:
            hasil += "100"
        elif angka == 5:
            hasil += "101"
        elif angka == 6:
            hasil += "110"
        else :
            hasil += "111"
        print(hasil, end="")
    else :
        temp1 = int(angka/8)
        konversi(temp1, hasil)
        temp2 = angka%8
        konversi(temp2, hasil)
    hasil =""
    konversi(16, hasil)
    
