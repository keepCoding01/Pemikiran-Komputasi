#nomor 3
N = int(input("Masukkan jumlah deret matematika yang ingin dibuat : "))
S = int(input("Masukkan bilangan awal : "))
D = int(input("Masukkan selisih bilangan : "))
bilangan = []

#proses
def indah(S,D,N):
    for i in range (N):
        bilangan.append(S+(i*D))
    return bilangan

#hasil
print(indah(S,D,N))

#algoritma
# mulai
# input nilai N,S,D
# inisialisasi/buat variable bilangan
# lakukan perulangan sebanyak n didalam fungsi indah, kemudian tambahkan setiap hasil proses kedalam variable bilangan
# kembalikan nilai bilangan
# print hasil
# selesai
    
    




