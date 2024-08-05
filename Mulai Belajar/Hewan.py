N = int(input())
X = [int(input()) for _ in range(N)]
Q = int(input())
Y = [int(input()) for _ in range(Q)]

totalHewan = 0
jenisHewan = [i for i in range(1, N+1)]
urutan_hewan = []

for i in range(N):
    totalHewan += X[i]

for i in range(totalHewan):
    for j in range(N):
        if X[j] > 0:
            urutan_hewan.append(jenisHewan[j])
            X[j] -= 1
            break

for y in Y:
    print(urutan_hewan[y-1])
