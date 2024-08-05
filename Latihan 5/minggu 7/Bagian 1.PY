def quick_sort(weights, low, high):
    if low < high:
        pivot = partition(weights, low, high)
        quick_sort(weights, low, pivot - 1)
        quick_sort(weights, pivot + 1, high)
    return weights


def partition(weights, low, high):
    pivot = weights[high]
    i = low - 1
    for j in range(low, high):
        if weights[j] <= pivot:
            i += 1
            weights[i], weights[j] = weights[j], weights[i]
    weights[i + 1], weights[high] = weights[high], weights[i + 1]
    return i + 1


def main():
    n = int(input("Enter the number of ducks: "))

    weights = []
    for i in range(n):
        weight = list(
            map(int, input(f"Enter the weight of duck {i + 1}: ").split()))
        weights.append(weight)

    weights = quick_sort(weights, 0, n - 1)

    print("\nThe weights of Pak Dengklek's ducks after sorting:")
    for i in range(n):
        print(f"Duck {i + 1}: {weights[i]}")


if __name__ == "__main__":
    main()
