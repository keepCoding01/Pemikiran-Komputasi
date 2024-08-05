n = int(input("Jumlah detik yang tersisa : "))
jam = n // 3600
n %= 3600
menit = n // 60
n %= 60
detik = n
print(f"{jam} Jam {menit} Menit {detik} Detik")
