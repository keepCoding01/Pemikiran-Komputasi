def katak_super():
    N = int(input("Masukkan jumlah balok kayu: "))
    ketinggian = list(
        map(int, input("Masukkan ketinggian balok kayu (dipisahkan spasi): ").split()))

    energi = [float('inf')] * N
    energi[0] = 0

    for i in range(N):
        if i + 1 < N:
            energi[i + 1] = min(energi[i + 1], energi[i] +
                                (ketinggian[i + 1] - ketinggian[i]) ** 2)
        if i + 2 < N:
            energi[i + 2] = min(energi[i + 2], energi[i] +
                                3 * (ketinggian[i + 2] - ketinggian[i]) ** 2)

    print(f"Energi minimum: {energi[N-1]}")


katak_super()
