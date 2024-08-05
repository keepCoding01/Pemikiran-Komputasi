v, h, n = map(int, input().split())
blok = [[] for _ in range(v+1)]
tabrakan = [0] * (h+2)

# mendapatkan koordinat batu-batu dan menyimpannya dalam list bloks

for i in range(n):
    v1, h1, v2, h2 = map(int, input(). split())
    for j in range(v1, v2+1):
        blok[j].append((h1, h2))

# menghitung jumlah tabrakan pada setiap kotak
for bloks in blok:
    for bloc in bloks:
        for tile in range(bloc[0], bloc[1] + 2):
            tabrakan[tile] += 1

# mencari nilai maksimum dari tabrakan
maxTabrak = max(tabrakan)

print(maxTabrak)
