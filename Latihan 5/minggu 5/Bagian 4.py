#ALGORITMA
#1. Lakukan fungsi def faktorial dengan parameter n
#2. jika n == 1, maka kembalikan nilai 1
#3. jika tidak maka kembalikan nilai n dikali fungsi faktorial (n-1)
#4. input nilai n
#5. cetak faktorial

#kompleksitas waktu = O(n)

def faktorial(n):
    if(n==1):
        return 1
    else:
        return n * faktorial(n-1)

n = int(input())
print(faktorial(n))
