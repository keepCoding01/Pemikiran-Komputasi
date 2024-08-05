# import sys
# def MatrixChainOrder(p, i, j):
#     if i == j:
#         return 0
#     _min = sys.maxsize

#     for k in range(i, j):
#         count = (MatrixChainOrder(p, i, k) +
#                  MatrixChainOrder(p, k+1, j) + p[i-1] * p[k] * p[j])
#         if count < _min:
#             _min = count
#     return _min


# if __name__ == '__main__':
#     arr = [1, 2, 3, 4, 3]
#     N = len(arr)

#     print("Minimum number of mnultiplications is ",
#           MatrixChainOrder(arr, 1, N-1))

# ////////////////////////////////////////////////////////////////////

# kompleksitas waktu = O(N^3)
# import sys
# dp = [[-1 for i in range(100) for j in range(100)]]


# def matrixChainMemoised(p, i, j):
#     if i == j:
#         return 0
#     if dp[i][j] != -1:
#         return dp[i][j]

#     dp[i][j] = sys.maxsize

#     for k in range(i, j):
#         dp[i][j] = min(dp[i][j], matrixChainMemoised(p, i, k) +
#                        matrixChainMemoised(p, k+1, j) + p[i-1] * p[k] * p[j])
#         return dp[i][j]


# def MatrixChainOrder(p, n):
#     i = i
#     j = n-1
#     return matrixChainMemoised(p, i, j)


# arr = [1, 2, 3, 4]
# n = len(arr)
# print("Jumlah minimum perkalian adalah ", MatrixChainOrder(arr, n))


# -------------------------------------------------------------
# kompleksitas O(N^3)
# import sys
# maxint = int(1e9+7)


# def MatrixChainOrder(p, n):
#     m = [[0 for x in range(n)] for x in range(n)]

#     for i in range(1, n):
#         m[i][i] = 0

#     for L in range(2, n):
#         for i in range(1, n-L+1):
#             j = i + L-1
#             m[i][j] = maxint
#             for k in range(i, j):
#                 q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
#                 if q < m[i][j]:
#                     m[i][j] = q
#     return m[1][n-1]


# arr = [1, 2, 3, 4]
# size = len(arr)

# print("Minimum number of multiplications is " +
#       str(MatrixChainOrder(arr, size)))

# ---------------------------------------------
# kompleksitas waktu : O(m*n)
def lcs(X, Y, m, n):
    L = [[None]*(n+1) for i in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i-j] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    return L[m][n]


if __name__ == '__main__':
    S1 = "AGGTAB"
    S2 = "GXTXAYB"
    m = len(S1)
    n = len(S2)
    print("Length of LCS is ", lcs(S1, S2, m, n))
