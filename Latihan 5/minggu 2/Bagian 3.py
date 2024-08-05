def waktuSisa(n):
    jam = n // 3600
    n %= 3600
    menit = n // 60
    detik = n % 60
    return jam, menit, detik
 
 
n = int(input("Masukkan jumlah detik yang tersisa: "))
jam, menit, detik = waktuSisa(n)
print(f"{jam} Jam {menit} Menit {detik} Detik")
 
