s = input()
koinBeda = -1

for i in range(len(s)):
    cari = True
    for j in range(len(s)):
        if i != j and s[i] == s[j]:
            cari = False
            break
    if cari:
        koinBeda = i+1
        break
print(koinBeda)
