# kompleksitas Big-O = O(N^2)
N = list(map(int, input().split()))
M = N[1]
K = []
Ktemp = []
temp = list(map(int, input().split()))
for i in range(N[0]):
    K.append(temp[i])
for i in range(N[0]):
    Ktemp.append(K[i])
MAP = []
for i in range(1, M+1):
    MAP.append(i)
Hasil = []
for i in range(N[0]):
    if Ktemp == []:
        for j in range(len(K)):
            Ktemp.append(K[j])
    Start = K[i]
    Langkah = 0
    while len(Ktemp) > 0:
        if Start in Ktemp:
            Ktemp.remove(Start)
        else:
            if Start+1 > M:
                Start = Start - (M)
            Start += 1
            Langkah += 1
    Hasil.append(Langkah)

    if Ktemp == []:
        for j in range(len(K)):
            Ktemp.append(K[j])
    Start = K[i]
    Langkah = 0
    while len(Ktemp) > 0:
        if Start in Ktemp:
            Ktemp.remove(Start)
        else:
            if Start-1 == 0:
                Start = M+1
            Start -= 1
            Langkah += 1
    Hasil.append(Langkah)

Min = 1000000000000
for i in range(len(Hasil)):
    if Hasil[i] < Min:
        Min = Hasil[i]
print(Min)
