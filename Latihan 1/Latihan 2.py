
# KOMPLEKSITAS : Big O(n^2) + Big O(n^3)

def prosesMatriks(n, matrix):
    for baris in matrix:
        print(*baris)


def main():
    n = int(input())
    semuaSimpul = []
    temp = []
    for i in range(n):
        simpul = input(f"")
        semuaSimpul.append(simpul)
        tetangga = input(f"")
        temp.append((simpul, tetangga))
    return n, semuaSimpul, temp


n, semuaSimpul, simpulTetangga = main()

matrix = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    simpul, daftarTetangga = simpulTetangga[i]
    for conn in daftarTetangga.split():
        j = semuaSimpul.index(conn)
        matrix[i][j] = 1
        matrix[j][i] = 1

prosesMatriks(n, matrix)
