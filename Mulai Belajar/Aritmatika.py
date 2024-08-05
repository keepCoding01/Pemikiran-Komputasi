n = int(input("Masukkan jumlah buah : "))
a = int(input("Masukkan jumlah Apel merah : "))
b = int(input("Masukkkan jumlah Apel hijau : "))

while b:
    a, b = b, a % b

minApel = n * (a // a)


print(minApel)
