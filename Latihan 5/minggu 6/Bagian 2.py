def MergeSort(arr):
 
    if len(arr) <= 1:
        return arr
 
    mid = len(arr) // 2
    kiri = MergeSort(arr[:mid])
    kanan = MergeSort(arr[mid:])
 
    return merge(kiri, kanan)
 
 
def merge(kiri, kanan):
 
    result = []
    i = j = 0
 
    while i < len(kiri) and j < len(kanan):
        if kiri[i] < kanan[j]:
            result.append(kiri[i])
            i += 1
        else:
            result.append(kanan[j])
            j += 1
 
    while i < len(kiri):
        result.append(kiri[i])
        i += 1
 
    while j < len(kanan):
        result.append(kanan[j])
        j += 1
 
    return result
 
 
def BinarySearch(arr, x):
    low = 0
    high = len(arr) - 1
 
    while low <= high:
        mid = (low + high) // 2
 
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else :
            return mid
 
    return -1
 
 
N = int(input("Masukkan jumlah baris = "))
X = list(map(int, input("Masukkan isi hewan per baris = ").split()))
Q = int(input("Masukkan jumlah pertanyaan = "))
Y = list(map(int, input("Masukkan angka urutan hewan = ").split()))
 
urutan = MergeSort(X)
 
for y in Y:
    index = BinarySearch(urutan, y)
    if index != -1:
        print(index + 1)
    else:
        print(-1)
        
        
# -------------------------------------------------------------------------------
def Mergesort(angka):
    print("Sebelum:", angka)
    if len(angka) <= 1:
        return angka
    mid = len(angka) // 2
    kiri = Mergesort(angka[:mid])
    kanan = Mergesort(angka[mid:])
    return merge(kiri,kanan)
 
def merge(kiri, kanan):
    merged = []
    i = 0
    j = 0
    while i < len(kiri) and j < len(kanan):
        if kiri[i] < kanan[j]:
            merged.append(kiri[i])
            i += 1
        else:
            merged.append(kanan[j])
            j += 1
    merged += kiri[i:]
    merged += kanan[j:]
    return merged
 
def binarySearch(angka, key):
    low = 0
    high = len(angka) - 1
    mid = 0
    status = False
    while low <= high:
        mid = (low + high) // 2
        if (key == angka[mid]):
            print(f"{key} ditemukan pada posisi ke- {mid +1} dan pada index ke-{mid}")
            status = True
            break
        else:
            if key > angka[mid]:
                low = mid + 1
            else:
                high = mid - 1
    if status == False:
        print(f"{key} tidak ditemukan dalam array")
    return

N = int(input("Masukkan jumlah baris = "))
X = list(map(int, input("Masukkan isi hewan per baris = ").split()))
Q = int(input("Masukkan jumlah pertanyaan = "))
Y = list(map(int, input("Masukkan angka urutan hewan = ").split()))
 
