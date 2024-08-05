n = int(input())
matrix = list(map(int, input().split()))
q = int(input())

memo = {}


def dp(start, end):
    if (start, end) in memo:
        return memo[(start, end)]

    a1 = 0
    a2 = 1
    a3 = 0

    for i in range(start+1, end):
        temp = matrix[start] * matrix[i] * matrix[end]

        res = dp(start, i)[0] + dp(i, end)[0] + temp
        if a1 == 0 or res < a1:
            a1 = res
            a2 = (dp(start, i)[1] * dp(i, end)[1]) % 26101991
        if res == a1:
            a2 = (a2 + dp(start, i)[1] * dp(i, end)[1]) % 26101991
        a3 = (a3+dp(start, i)[2] * dp(i, end)[2]) % 26101991
    if a3 == 0:
        a3 = 1
    memo[(start, end)] = (a1, a2, a3)
    return (a1, a2, a3)


a1, a2, a3 = dp(0, len(matrix)-1)

if q == 1:
    print(a1)
elif q == 2:
    print(a2)
elif q == 3:
    print(a3)
