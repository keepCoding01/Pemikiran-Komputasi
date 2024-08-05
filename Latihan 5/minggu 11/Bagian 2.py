# kompleksitas = big o = O(n)
N = int(input())
SCORE = []
CANDY = []
for i in range(N):
    temp = int(input())
    SCORE.append(temp)
for i in range(N):
    CANDY.append(1)
for i in range(1, N):
    if SCORE[i] > SCORE[i-1]:
        CANDY[i] = CANDY[i-1] + 1
for i in range(N-2, -1, -1):
    if SCORE[i] > SCORE[i+1] and CANDY[i] <= CANDY[i+1]:
        CANDY[i] = CANDY[i] + CANDY[i+1]

Hasil = 0
for i in range(len(CANDY)):
    Hasil = Hasil + CANDY[i]
print(Hasil)
