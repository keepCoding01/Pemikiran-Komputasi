# Algoritma
# 1. Mulai
# 2. Input kalimat
# 3. Inisialisasi list berisi nilai kalimat ke dalalm variabel karakter
# 4. Lakukan perulangan i pada tiap karakter 
# 5. Lakukan perulangan j dimulai dari indeks 1 sepanjang karakter
# 6. Jika karakter kode ASCiI i lebih besar dari karakter kode ASCII j, tukar karakter i dengan j
# 7. Buat variabel urutan dan tambahkan nilai dari variable karakter
# 8. Masukkan nilai urutan kedalam variable kata dan split kan
# 9. Lakukan perulangan i sepanjang kata
# 10.Inisialisasi kembali nilai kedalam variable kata
# 11. Masukkan variable nilai kata ke dalam urutan dalam bentuk string
# 12. Cetak urutan
# 13. Selesai

# Kompleksitas waktu = O(n^2) + O(n)
 


kalimat = input("Masukkan kalimat = ")
 
karakter = list(kalimat)
 
for i in range(len(karakter)):
    for j in range(i + 1, len(karakter)): 
        if ord(karakter[i]) > ord(karakter[j]):      
            karakter[i], karakter[j] = karakter[j], karakter[i]
 
urutan = ''.join(karakter)
 
kata = urutan.split()
for i in range(len(kata)):
    kata[i] = kata[i]
 
urutan = ' '.join(kata)
 
print(urutan)



