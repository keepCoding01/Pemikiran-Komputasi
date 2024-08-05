def quick_sort(names, low, high):
    if low < high:
        pivot = partition(names, low, high)
        quick_sort(names, low, pivot - 1)
        quick_sort(names, pivot + 1, high)
    return names


def partition(names, low, high):
    pivot = len(names[high])
    i = low - 1
    for j in range(low, high):
        if len(names[j]) <= pivot:
            i += 1
            names[i], names[j] = names[j], names[i]
    names[i + 1], names[high] = names[high], names[i + 1]
    return i + 1


def main():
    n = int(input("Masukkan jumlah orang: "))

    names = []
    for i in range(n):
        name = input(f"Masukkan nama orang {i + 1}: ")
        names.append(name)

    names = quick_sort(names, 0, n - 1)

    print("\nDaftar nama yang sudah diurutkan berdasarkan jumlah huruf:")
    for i in range(n):
        print(f"{names[i]}")


if __name__ == "__main__":
    main()
