def min_nilai(N, K, arr):
    arr.sort()
    min_diff = float('inf')

    for i in range(N-K+1):
        current_diff = arr[i + K - 1] - arr[i]
        if current_diff < min_diff:
            min_diff = current_diff

    return min_diff


N, K = map(int, input().split())
array = list(map(int, input(). split()))

hasil = min_nilai(N, K, array)
print(hasil)
