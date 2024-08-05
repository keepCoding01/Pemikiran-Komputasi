kalimat = str(input("Masukkan kalimat = "))

huruf = []

for char in kalimat:
    if char.isalpha():
        huruf.append(char)

huruf.sort()

hasil = ''.join(huruf)
print(hasil)
