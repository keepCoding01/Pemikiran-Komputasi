# ALGORITMA
# inisialisasi fungsi tetanggaSimpul dengan parameter n dan temp
# buat list tetangga yang berisi n list kosong
# lakukan perulangan dari setiap simpul, ambil tetangga simpul dari temp dan pecah menjadi list, kemudian simpan di list tetangga
# buat list output dan isi dengan string yang menyatakan tetangga dari setiap simpul
# lakukan perulangan dari setiap simpul dan gabungkan list tetangga
# kembalikan list output yang berisi hasil
# inisialisasi fungsi main
# lakukan inputan jumlah simpul
# buat list temp yang kosong
# lakukan perulangan sebanyak n kali, kemudian ambil simpul dan tetangganya dan tambahkan ke temp
# kembalikan nilai n dan temp
# panggil fungsi main dan simpan hasilnya ke n dan temp
# panggil fungsi tetanggaSimpul dengan parameter n dan temp, kemudian simpan hasilnya ke output
# cetak tiap elemen output dipisahkan dengan baris baru


# kompleksitas :
# - fungsi tetanggaSimpul = Big O(n*k)
# - fungsi main = Big O(n*t)
# - total = Big O(n*t) + Big O(n*k) + Big O(n*1)

def tetanggaSimpul(n, temp):
    tetangga = [[] for _ in range(n)]
    for i in range(n):
        simpul = temp[2 * i]
        tetanggaSimpul = temp[2 * i + 1].split()
        tetangga[i] = tetanggaSimpul

    output = []
    for i in range(n):
        output.append(
            f"Tetangga dari {temp[2 * i]} adalah {' '.join(tetangga[i])}")
    return output


def main():
    n = int(input())
    temp = []
    for i in range(n):
        simpul = input(f"")
        tetanggaSimpul = input(f"")
        temp.extend([simpul, tetanggaSimpul])
    return n, temp


n, temp = main()
output = tetanggaSimpul(n, temp)
print("\n".join(output))
