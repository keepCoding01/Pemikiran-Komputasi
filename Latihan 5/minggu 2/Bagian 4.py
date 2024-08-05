def minApel(n, a, b):
    minimal = min(a, b)
    a //= minimal
    b //= minimal
    hasil = n * (a + b - 1) // (2 * minimal)
    if hasil % 2 == 1:
        hasil += 1
    return hasil // 2
 
 
def min(a, b):
    while b:
        a, b = b, a % b
    return a
 
 
if __name__ == "__main__":
    n = int(input("Masukkan jumlah apel: "))
    a = int(input("Berat apel merah: "))
    b = int(input("Berat apel hijau: "))
    hasil = minApel(n, a, b)
    print(f"Minimal jumlah apel dimakan: {hasil}")
