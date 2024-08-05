n = int(input())
huruf = input()

if n < 3:
    print(-1)
else:
    max_lampu = -1

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if huruf[i] != huruf[j] and huruf[j] != huruf[k] and huruf[i] !=
                count = 3
                idx = k
                while idx < n:
                    if huruf[idx] == huruf[idx-3]:
                        count += 1
                        idx += 1
                    else:
                        break
                max_lampu = max(max_lampu, count)

        print(max_lampu if max_lampu != -1 else -1)
