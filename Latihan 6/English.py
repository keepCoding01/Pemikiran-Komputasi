# ALGORITMA

# 1. IMPORT HEAPQ, RANDOM, DATETIME, TIMEDELTA, TABULATE, FRACTION.
# 2. BUAT LIST station, DICT SELURUH route DAN DICT train DIDALAM LIST.
# 3. INISIALISASI DEF DJIKSTRA DENGAN 3 PARAMETER (route, begin, end).
# 	- INISIALISASI queue DENGAN LIST YANG MENGISI TIAP PARAMETER DJIKSTRA.
# 	- SET visited DENGAN FUNGSI SET().
# 	- LAKUKAN PERULANGAN queue SELAMA KONDISI TERPENUHI.
# 	- INISIALISASI routeDuration, station, JALUR KE DALAM VARIABEL queue YANG TELAH DIBUAT SEBELUMNYA.
# 	- JIKA station TERMASUK DALAM visited, TERUSKAN PROGRAM.
# 	- TAMBAHKAN station KE DALAM visited.
# 	- TAMBAHKAN JALUR DENGAN station UNTUK DIMASUKKAN NILAINYA KE DALAM JALUR.
# 	- JIKA station == end, KEMBALIKAN NILAI routeDuration DAN JALUR.
# 	- SELAMA nextStation DAN distance BERADA DIDALAM route, AMBIL NILAI station PER-ITEM.
# 	- JIKA nextStation TIDAK ADA DI visited,
#   - TAMBAHKAN NILAI YANG ADA DIDALAM routeDuration+distance, nextStation, JALUR KE DALAM queue.
#   - TAMBAHKAN KE BAGIAN BELAKANG.
# 	- KEMBALIKAN NILAINYA.
# 4. INISIALISASI DEF VIEWTRAIN.
# 	- LAKUKAN PERULANGAN SELAMA KONDISI BENAR.
# 	- INISIALISASI table.
# 	- LAKUKAN PERULANGAN train SELAMA NILAI YANG ADA DIDALAM VARIABLE train.
# 	- BUAT table MENGGUNAKAN TABULATE.
# 	- JIKA PENGGUNA TIDAK INGIN DIBERIKAN goodsCarried ALIAS MENGINPUT "TIDAK",
#   - MAKA BERIKAN STEP BERIKUTNYA: TANYA trainClassName DAN KEMUDIAN KELUAR DARI MENU VIEWTRAIN.
# 	- JIKA PENGGUNA MENGINPUT DATA YANG SALAH (DILUAR DARI KATA YA/TIDAK),
#   - BERIKAN KESEMPATAN UNTUK MENGULANG YANG BENAR.
# 	- JIKA PENGGUNA INGIN DIBERIKAN goodsCarried ALIAS MENGINPUT "YA",
#   - MAKA BERIKAN STEP BERIKUTNYA YAITU TANYAKAN trainClassName API YANG INGIN DICOBA.
# 	- CETAK PENJELASAN UNTUK MEMBERIKAN NILAI PRIORITAS MASING-MASING BARANG.
# 	- TANYAKAN BERAPA BANYAK BARANG YANG INGIN DIBAWA.
# 	- LAKUKAN PERULANGAN I SEPANJANG amountOfGoods + 1.
# 	- CETAK FORMAT UNTUK MEMBUAT DATA BARANG KEMUDIAN MASUKKAN KE items.
# 	- CETAK DAN INPUT APAKAH BARANG INGIN DIPECAH?.
# 	- JIKA YA, MAKA LANJUTKAN FUNGSI FRACTIONALKNAPSACK.
# 	- JIKA TIDAK, MAKA LANJUTKAN FUNGSI ONEZEROKNAPSACK.
# 	- TANYAKAN APAKAH INGIN MENCOBA KELAS LAIN?
# 	- JIKA YA, MAKA ULANGI DEF VIEWTRAIN, JIKA TIDAK MAKA PROGRAM BERHENTI.
# 5. INISIALISASI DEF ONEZEROKNAPSACK DENGAN 2 PARAMETER (selectedTrainClass,items)
# 	- INISIALISASI NILAI totalWeight = 0
# 	- INISIALISASI NILAI totalValue = 0
# 	- INISIALISASI NILAI itemRecommendation DENGAN LIST KOSONG
# 	- LAKUKAN PERULANGAN NAMA,BERAT,PRIORITAS SELAMA NILAINYA ADA DI VARIABEL items.
# 	- JIKA selectedTrainClass LEBIH KECIL SAMA DENGAN 0, HENTIKAN.
# 	- JIKA BERAT <= selectedTrainClass,
#   - TAMBAHKAN BERAT KE VARIABEL totalWeight DAN TAMBAHKAN NILAI PRIORITAS KE DALAM VARIABEL totalValue.
# 	- TAMBAHKAN NAMA KE DALAM itemRecommendation.
# 	- KURANGKAN BERAT DENGAN NILAI selectedTrainClass KEMUDIAN MASUKKAN NILAINYA DI selectedTrainClass.
# 	- CETAK KAMI MEREKOMENDASIKAN KAMU UNTUK MEMBAWA :.
# 	- LAKUKAN PERULANGAN UNTUK MENCETAK NOMOR DAN NAMA BARANG.
# 	- CETAK BERAT TOTAL BARANG YANG DIBAWA DARI NILAI YANG ADA DI VARIABEL TOTAL BERAT.
# 6. INISIALISASI DEF FRACTIONALKNAPSACK DENGAN 2 PARAMETER (selectedTrainClass, items).
# 	- MENGURUTKAN items.
# 	- INISIALISASI VARIABEL totalWeight DAN totalValue DENGAN NILAI 0.
# 	- INISIALISASI VARIABEL itemRecommendation DENGAN LIST KOSONG.
# 	- LAKUKAN PERULANGAN NAMA,BERAT,PRIORITAS SELAMA NILAINYA ADA DI items.
# 	- JIKA BERAT <= selectedTrainClass,
#   - KURANGKAN BERATNYA DAN TAMBAHKAN BERAT KE TOTAL BERAT SERTA PRIORITAS KE TOTAL NILAI.
# 	- TAMBAHKAN NILAI YANG ADA DI VARIABEL NAMA DIIKUTI DENGAN KATA whole DI itemRecommendation.
# 	- JIKA TIDAK, INISIASLISASI NILAI bestItem DENGAN NONE DAN URUTKAN items.
# 	- SELAMA ITEM ADA DI sortItems, JIKA ITEM PADA INDEKS PERTAMA LEBIH KECIL DARI selectedTrainClass, HITUNG fractionNYA.
# 	- MASUKKAN NILAI weightTaken KE DALAM totalWeight.
# 	- MASUKKAN HASIL PERKALIAN DARI ITEM PADA INDEKS KEDUA DENGAN fraction KE DALAM totalValue.
# 	- JIKA fraction SAMA DENGAN 1, MAKA CETAK whole. JIKA TIDAK MAKA CETAK NILAI PECAHAN MENGGUNAKAN LIBRARY FRACTION.
# 	- TAMBAHKAN NILAINYA KEDALAM VARIABEL itemRecommendation.
# 	- KURANGKAN NILAI ITEM DI INDEKS PERTAMA DENGAN BERAT YANG DIAMBIL DAN MASUKKAN KEDALAM remainWeight.
# 	- JIKA remainWeight > 0, HAPUS ITEM items DAN ITEM INDEKS-0, remainWeight DAN ITEM PADA INDEKS-2, KE remainWeight.
# 	- HENTIKAN PROGRAM.
# 	- JIKA bestItem, LAKUKAN PENGURANGAN INDEKS PERTAMA-1 PADA bestItem DAN TAMBAHKAN KEDALAM selectedTrainClass.
# 	- TAMBAHKAN INDEKS-1 bestItem KE totalWeight DAN TAMBAH INDEKS-2 bestItem KE totalValue.
# 	- MASUKKAN INDEKS KE NOL DENGAN KATA whole KEDALAM itemRecommendation.
# 	- JIKA TIDAK, MASUKKAN NILAI DARI selectedTrainClass KEDALAM SISAKAPASITAS.
# 	- BAGI NILAI SISAKAPASITAS DENGAN BERAT DAN MASUKKAN NILAINYA KEDALAM VARIABEL fraction.
# 	- KALIKAN NILAI fraction DENGAN BERAT DAN TAMPUNG NILAINYA KE DALAM weightTaken.
# 	- TAMBAHKAN NILAI weightTaken KE DALAM VARIBEL totalWeight.
# 	- TAMBAHKAN HASIL PERKALIAN fraction DENGAN PRIORITAS KE DALAM VARIABEL totalValue.
# 	- MASUKKAN NILAI NAMA DAN fraction KE DALAM itemRecommendation.
# 	- KURANGKAN NILAI weightTaken DENGAN selectedTrainClass.
# 	- LAKUKAN PERULANGAN ITEM SELAMA NILAINYA ADA PADA items.
# 	- JIKA ITEM PADA INDEKS PERTAMA LEBIH KECIL SAMA DENGAN selectedTrainClass,
#   - HAPUS ITEM PADA items DAN MASUKKAN KEMBALI PADA POSISI PERTAMA.
# 	- JIKA selectedTrainClass BUKAN LEBIH BESAR DARI NOL, HENTIKAN PROGRAM TERSEBUT.
# 	- CETAK KAMI MEREKOMENDASIKAN BARANG YANG DAPAT DIBAWA.
# 	- LAKUKAN PERULANGAN UNTUK MENCETAK HASILNYA.
# 	- CETAK BERAT TOTAL BARANG YANG DIBAWA.
# 7. INISIALISASI FUNGSI VIEWROUTES.
# 	- INISIASASI stationS DENGAN LIST UNTUK route ALIAS AMBIL NILAI KEYNYA.
# 	- INISIALISASI VARIABEL TELAHDITAMPILKAN DENGAN NILAI SET.
# 	- INISIALISASI VARIABEL UNTUK table.
# 	- LAKUKAN PERULANGAN SELAMA begin ADA NILAINYA DI stationS.
# 	- LAKUKAN PERULANGAN end DARI INDEKS begin DI route.
# 	- JIKA VAR begin DAN end TIDAK ADA DI TELAHDITAMPILKAN, BEGITU JUGA SEBALIKNYA,
#   - INISIALISASI routeDuration UNTUK MENAMPUNG NILAI route DI INDEKS begin DAN end.
# 	- INISIALISASI table DENGAN FUNGSI TABULATE UNTUK MENCETAK route DAN duration.
# 	- LAKUKAN PERULANGAN SELAMA KONDISI BENAR.
# 	- CETAK MASUKKAN route KAMU.
# 	- INPUT NILAI originStation DAN destination.
# 	- JIKA originStation TIDAK ADA DI DAFTAR stationS, CETAK station availed. SILAKAN COBA LAGI.
# 	- PANGGIL FUNGSI DJIKSTRA DAN TAMPUNG NILAINYA DI VARIABEL routeDuration DAN JALUR.
# 	- JIKA routeDuration NILAINYA TAK HINGGA, CETAK TIDAK ADA route YANG TERSEDIA.
# 	- JIKA TIDAK, PRINT JALUR TERPENDEKNYA.
# 	- JIKA INPUT LIHAT route LAIN BUKAN 'YA', HENTIKAN PROGRAM TERSEBUT.
# 8. INISIALISASI DEF ORDERTICKET.
# 	- CETAK PASTIKAN ANDA TELAH MEMERIKSA route SEBELUM MEMESAN TIKET DAN TANYAKAN KEMANA AKAN PERGI.
# 	- INPUT NILAI originStation DAN destination.
# 	- JIKA station ASAL TIDAK ADA DI DAFTAR station, CETAK station availed DAN KEMBALIKAN NILANYA.
# 	- PANGGIL FUNGSI DJIKSTRA DAN TAMPUNG KE DALAM VARIABEL routeDuration DAN track.
# 	- JIKA NILAI routeDuration INF, CETAK TIDAK ADA route YANG TERSEDIA DAN KEMBALIKAN NILAI.
# 	- CETAK route PERJALANAN TERPENDEK.
# 	- LAKUKAN PERULANGAN SELAMA KONDISI BENAR.
# 	- CETAK PASTIKAN ANDA TELAH MEMERIKSA BARANGBAWAAN ANDA SEBELUM MEMILIH KELAS.
# 	- INPUT NILAI trainClassAPI.
# 	- JIKA TULISANNYA LOWER SEMUA, MAKA CAPITALIZE DAN BREAK.
# 	- JIKA TIDAK, CETAK trainClassName YANG ANDA MASUKKAN SALAH. SILAKAN COBA LAGI.
# 	- CETAK SILAKAN MASUKKAN DATA ANDA.
# 	- MASUKKAN DATA name, date, time DAN confirmation.
# 	- INISIALISASI numberTrain, train, platform, seat DENGAN NILAI ACAK MENGGUNAKAN FUNGSI RANDOM.
# 	- INISIALISASI FORMAT timeArrive DAN travelTime.
# 	- INISIALISASI travelTime DENGAN TP DAN WP.
# 	- INISIALISASI timeArrive DENGAN TT DAN WT.
# 	- HITUNG totalCost DENGAN MENGALIKAN 15 DENGAN routeDuration + train.
# 	- JIKA KONFIRMASI SAMA DENGAN 'YA', CETAK FORMAT TIKET.
# 	- CETAK TOTAL BIAYA MELALUI VARIABEL totalCost.
# 	- JIKA PESAN TIKET LAGI DIINPUT YA, MAKA JALANKAN KEMBALI DEF ORDERTICKET.
# 	- JIKA BUKAN, MAKA BERHENTI DAN CETAK PEMESANAN TIKET DIBATALKAN. SILAKAN COBA LAGI.
# 9. INISIALISASI DEF mainMenu.
# 	- CETAK SELAMAT DATANG DI PROGRAM PEMESANAN TIKET KERETA API.
# 	- INPUT NAMA DEPAN.
# 	- LAKUKAN PERULANGAN SELAMA KONDISI BENAR.
# 	- CETAK SELAMAT DATANG DI (NAMA KITA) EXPRESS.
# 	- CETAK SEMUA MENU (PESAN TIKET, LIHAT route, LIHAT train, KELUAR).
# 	- INPUT UNTUK MEMILIH choice MENU.
# 	- JIKA MEMILIH 1, JALANKAN FUNGSI ORDERTICKET.
# 	- JIKA MEMILIH 2, JALANKAN FUNGSI VIEWROUTES.
# 	- JIKA MEMILIH 3, JALANKAN FUNGSI VIEWTRAIN.
# 	- JIKA MEMILIH 4, CETAK TERIMA KASIH TELAH MENGGUNAKAN PROGRAM KAMI. HENTIKAN PROGRAM.
# 	- JIKA BUKAN SEMUANYA, CETAK choice availed. SILAKAN COBA LAGI.
# 10. JALANKAN FUNGSI mainMenu.

# TOTAL KOMPLEKSITAS WAKTU
# T(n) = O((V + E)log V + n log n)
# CATATAN :
# PADA SETIAP FUNGSI, AKAN DIPILIH WAKTU YANG PALING EFEKTIF DAN EFISIEN.
# FUNGSI YANG PALING BAGUS ADA DI ALGORITMA DJIKSTRA DAN FRACTIONAL KNAPSACK DI DALAM MENU orderTicket(), viewRoutes() DAN 'viewTrain()'.
# SEHINGGA, KOMPLEKSITAS WAKTU SECARA KESELURUHAN YANG DIDAPAT MERUPAKAN PENGGABUNGAN ANTARA ALGORITMA DJIKSTRA DAN FRACTIONAL KNAPSACK.


# TOTAL KOMPLEKSITAS RUANG
# S(n) = O(V + E + n)
# PADA SETIAP FUNGSI, AKAN DIPILIH RUANG YANG PALING BESAR.
# FUNGSI DENGAN PENGGUNAAN RUANG TERBESAR ADA PADA  djikstra(), viewRoutes(), oneZeroKnapsack() DAN fractionalKnapsack().
# SEHINGGA,KOMPLEKSITAS RUANG SECARA KESELURUHAN YANG DIDAPAT MERUPAKAN PENGGABUNGAN ANTARA KEEMPAT FUNGSI TERSEBUT.


import heapq
import random
from datetime import datetime, timedelta
# jika ingin menggunakan kode program ini, pastikan sudah menginstall "pip install tabulate" di terminal.
from tabulate import tabulate
# import fraction ini, bukan berarti langsung membagi menjadi pecahan. namun merubah bilangan desimal (0,5) menjadi pecahan (1/2).
from fractions import Fraction

stations = ['Minstowe', 'Oldcastle', 'Cowstone',
            'New North', 'Freeham', 'Bingborough', 'Donningpool', 'Old Mere', 'Highbrook', 'Wington']
route = {
    "Minstowe": {"Cowstone": 3},
    "Oldcastle": {"New North": 5, "Freeham": 2},
    "Cowstone": {"Minstowe": 3, "New North": 4, "Bingborough": 6, "Donningpool": 7, "Highbrook": 5, "Freeham": 2},
    "New North": {"Oldcastle": 5, "Cowstone": 4, "Bingborough": 3, "Donningpool": 6, "Wington": 4, "Highbrook": 2},
    "Freeham": {"Oldcastle": 2, "Cowstone": 2, "Donningpool": 3, "Wington": 5},
    "Bingborough": {"Cowstone": 6, "New North": 3, "Donningpool": 2, "Highbrook": 1},
    "Donningpool": {"Cowstone": 7, "New North": 6, "Freeham": 3, "Bingborough": 2, "Wington": 4, "Highbrook": 5, "Old Mere": 2},
    "Highbrook": {"Cowstone": 5, "New North": 2, "Bingborough": 1, "Donningpool": 5},
    "Wington": {"New North": 4, "Freeham": 5, "Donningpool": 4},
    "Old Mere": {"Donningpool": 2}
}

train = [
    {'trainClassName': 'Economy',
        'trainCapacity': 25, 'trainClassPrices': 20},
    {'trainClassName': 'Business',
        'trainCapacity': 30, 'trainClassPrices': 30},
    {'trainClassName': 'Exclusive',
        'trainCapacity': 35, 'trainClassPrices': 40}
]


# T(n) = O((V + E)log V)
# S(n) = O(V)
def dijkstra(route, begin, end):
    queue = [(0, begin, [])]
    visited = set()
    while queue:
        routeDuration, station, track = heapq.heappop(queue)
        if station in visited:
            continue
        visited.add(station)
        track = track + [station]
        if station == end:
            return routeDuration, track
        for nextStation, distance in route.get(station, {}).items():
            if nextStation not in visited:
                heapq.heappush(
                    queue, (routeDuration + distance, nextStation, track))
    return float("inf"), []


# T(n) = O(n)
# S(n) = O(n)
def viewTrain():
    while True:
        table = []
        for trainn in train:
            table.append([trainn['trainClassName'],
                         trainn['trainCapacity'], trainn['trainClassPrices']])
        print(tabulate(table, headers=[
              'Train Name', 'Capacity (kg)', 'Price ($) per kg'], tablefmt="grid"))
        goodsCarried = input(
            "we can help you choose what to bring, whether you want to try ?\nyes/no = ")
        if goodsCarried == "no":
            while True:
                trainClass = input("Select Class : ").capitalize()
                if trainClass in ['Economy', 'Business', 'Exclusive']:
                    break
                else:
                    print(
                        "The train class you selected is invalid. Please try again.")

            selectedTrainClass = next(
                (trainn for trainn in train if trainn['trainClassName'] == trainClass), None)

            if not selectedTrainClass:
                print("The train class you selected is not available.")
                return

            selectedTrainClass = selectedTrainClass.copy()
            break

        elif goodsCarried not in ["no", "yes"]:
            print("you entered it wrong. try again")
            viewTrain()

        while True:
            trainClass = input("Select Class : ").capitalize()
            if trainClass in ['Economy', 'Business', 'Exclusive']:
                break
            else:
                print("The train class you selected is invalid. Please try again.")

        selectedTrainClass = next(
            (trainn for trainn in train if trainn['trainClassName'] == trainClass), None)

        if not selectedTrainClass:
            print("The train class you selected is not available.")
            return

        selectedTrainClass = selectedTrainClass.copy()

        if goodsCarried == "yes":
            items = []
            print(
                "Give your items a priority scale ranging from 1 (very important) to 5 (not important)")
            amountOfGoods = int(
                input("How many items do you want to bring? "))

            for i in range(1, amountOfGoods + 1):
                print(f"\nItem-{i}")
                name = input(f"Name of Item-{i}\t\t\t: ")
                weight = float(input(f"Weight of Item-{i} (kg)\t\t: "))
                priority = int(input(f"Priority Of Item-{i} (1-5)\t: "))
                items.append((name, weight, priority))
            canBeSplit = input(
                "\nDo you want to break an item into several pieces? (Yes/No): ").lower() == 'yes'

            if canBeSplit:
                fractionalKnapsack(selectedTrainClass, items)
            else:
                oneZeroKnapsack(selectedTrainClass, items)

        if input("\nWant to try another class? (Yes/No): ").lower() != 'yes':
            break


# T(n) = O(n)
# S(n) = O(n)
def oneZeroKnapsack(selectedTrainClass, items):
    totalWeight = 0
    totalValue = 0
    itemRecommendations = []

    for name, weight, priority in items:
        if selectedTrainClass['trainCapacity'] <= 0:
            break

        if weight <= selectedTrainClass['trainCapacity']:
            totalWeight += weight
            totalValue += priority

            itemRecommendations.insert(0, (name))
            selectedTrainClass['trainCapacity'] -= weight

    print("\nWe recommend you to bring :")
    for idx, item in enumerate(itemRecommendations, start=1):
        print(f"{idx}. {item}")
    print(f"\nTotal weight of items carried: {totalWeight} kg")


# T(n) = O(n log n)
# S(n) = O(n)
def fractionalKnapsack(selectedTrainClass, items):
    items.sort(key=lambda x: x[1], reverse=True)

    totalWeight = 0
    totalValue = 0
    itemRecommendations = []

    for name, weight, priority in items:
        if selectedTrainClass['trainCapacity'] > 0:
            if weight <= selectedTrainClass['trainCapacity']:
                selectedTrainClass['trainCapacity'] -= weight
                totalWeight += weight
                totalValue += priority
                itemRecommendations.append((name, "whole"))
            else:
                bestItem = None
                sortItems = sorted(
                    items, key=lambda x: x[1])
                for item in sortItems:
                    if item[1] <= selectedTrainClass['trainCapacity']:
                        fraction = min(
                            1, selectedTrainClass['trainCapacity'] / item[1])
                        weightTaken = fraction * item[1]
                        totalWeight += weightTaken
                        totalValue += item[2] * fraction
                        if fraction == 1:
                            fractionLabel = "whole"
                        else:
                            fractionLabel = str(
                                Fraction(fraction).limit_denominator())

                        itemRecommendations.append(
                            (item[0], fractionLabel))
                        selectedTrainClass['trainCapacity'] -= weightTaken

                        remainWeight = item[1] - weightTaken
                        if remainWeight > 0:
                            items.remove(item)
                            items.append(
                                (item[0], remainWeight, item[2]))

                        break

                if bestItem:
                    selectedTrainClass['trainCapacity'] -= bestItem[1]
                    totalWeight += bestItem[1]
                    totalValue += bestItem[2]
                    itemRecommendations.append(
                        (bestItem[0], "whole"))
                    items.remove(bestItem)
                else:
                    remainCapacity = selectedTrainClass['trainCapacity']
                    fraction = remainCapacity / weight
                    weightTaken = fraction * weight
                    totalWeight += weightTaken
                    totalValue += priority * fraction
                    itemRecommendations.append(
                        (name, str(Fraction(round(fraction, 2)).limit_denominator())))
                    selectedTrainClass['trainCapacity'] -= weightTaken

                    for item in items:
                        if item[1] <= selectedTrainClass['trainCapacity']:
                            items.remove(item)
                            items.insert(0, item)
                            break

        else:
            break

    print("\nWe recommend items you can bring :")

    for idx, item in enumerate(itemRecommendations, start=1):
        nameItem = item[0].capitalize()
        labelFr = item[1]

        if labelFr == "whole":
            print(f"{idx}. {nameItem} (whole)")
        else:
            print(f"{idx}. {nameItem} ({labelFr})")
    print(f"\nTotal weight of items carried: {totalWeight} kg")


# T(n) = O(V + E)
# S(n) = O(V + E)
def viewRoutes():
    stations = list(route.keys())
    displayed = set()
    table = []
    for begin in stations:
        for end in route[begin]:
            if (begin, end) not in displayed and (end, begin) not in displayed:
                routeDuration = route[begin][end]
                table.append([f"{begin} -- {end}", routeDuration])
                displayed.add((begin, end))
    print("\nCost : $15/jam")
    print(tabulate(table, headers=[
          "Routes (2-way)", "Duration (Hours)"], tablefmt="outline"))

    while True:
        print("Enter your route")
        print("====================")
        originStation = input("\nFrom : ")
        destinationStation = input("To   : ")
        if originStation not in stations or destinationStation not in stations:
            print("Invalid station. Please try again.")
            continue

        routeDuration, track = dijkstra(
            route, originStation, destinationStation)
        if routeDuration == float("inf"):
            print("No routes available.")
        else:
            print(
                f"\nThis is the shortest route from {originStation} to {destinationStation}:\n{' -> '.join(track)}\nDuration: {routeDuration} hours")

        if input("\nSee another route? (Yes/No): ").lower() != 'yes':
            break


# T(n) = O(1)
# S(n) = O(V)
def orderTicket():
    print("\nMake sure you have checked the route before booking tickets.\nWhere are you going ?")
    originStation = input("From : ")
    destinationStation = input("To   : ")
    if originStation not in stations or destinationStation not in stations:
        print("Invalid station.")
        return

    routeDuration, track = dijkstra(route, originStation, destinationStation)
    if routeDuration == float("inf"):
        print("No routes available.")
        return

    print(
        f"\nThis is the travel route from {originStation} to {destinationStation}: \n{' -> '.join(track)} \nDuration: {routeDuration} hours")

    while True:
        print("\nMake sure you have checked your luggage before choosing a class.")
        trainClassInput = input(
            "Select class (Economy, Business, Exclusive): ")
        if trainClassInput.lower() in ['economy', 'business', 'exclusive']:
            trainClass = trainClassInput.capitalize()
            break
        else:
            print("The train class you entered is incorrect. Please try again.")

    print("\nPlease enter your data : ")
    name = input("Enter your name\t\t\t\t: ")
    date = input("Enter the departure date (DD/MM/YYYY)\t: ")
    time = input("Enter departure time (HH:MM)\t\t: ")
    confirmation = input("Is your data correct? (Yes/No)\t\t: ")

    trainNumber = random.randint(000, 999)
    platform = f"{random.randint(1, 10):02}"
    trainClassPrice = next(trainClass['trainClassPrices']
                           for trainClass in train if trainClass['trainClassName'].lower() == trainClassInput.lower())
    seat = random.randint(1, 50)
    timeArrive = datetime.strptime(
        date + ' ' + time, '%d/%m/%Y %H:%M') + timedelta(hours=routeDuration)
    travelTime = datetime.strptime(
        date + ' ' + time, '%d/%m/%Y %H:%M')

    tp = travelTime.strftime(
        '%d/%m/%Y')
    wp = travelTime.strftime('%H:%M')
    tt = timeArrive.strftime('%d/%m/%Y')
    wt = timeArrive.strftime('%H:%M')
    totalCost = 15 * routeDuration + trainClassPrice

    if confirmation.lower() == 'yes':
        print(f'''
+------------------------------------------------------------+
| MELLOW TRAIN TICKETS                                       |
+------------------------------------------------------------+
| ORIGIN         : {originStation}                                  |
+------------------------------------------------------------+
| DATE           : {tp}            TIME  : {wp}       |
| TRAIN#         : {trainNumber}                   CLASS : {trainClass}   |
| PLATFORM       : {platform}                    SEAT  : {seat}          |
+------------------------------------------------------------+
| DESTINATION    : {destinationStation}                                  |
+------------------------------------------------------------+
| DATE           : {tt}            TIME : {wt}        |
+------------------------------------------------------------+
| PASSENGER NAME : {name}                                     |
+------------------------------------------------------------+
''')
        print(f"Total cost : ${totalCost}")
        if input("\nOrdering more tickets? (Yes/No): ").lower() != "Yes":
            pass
        else:
            orderTicket()
    else:
        print("\nTicket order cancelled. Please try again.")


# T(n) = Tergantung fungsi yang dipanggil dalam loop
# S(n) = Tergantung fungsi yang dipanggil
def mainMenu():
    print("================================================================")
    print("Welcome to the Train ticket booking program")
    name = input("\nBefore using the program, enter your first name: ")
    print("================================================================")
    while True:
        print(f"\nWelcome to {name} Express")
        print("===================================")
        print("1. Order Ticket")
        print("2. View Routes")
        print("3. View Train")
        print("4. Exit")
        print("===================================")
        choice = input("choose (1-4): ")

        if choice == '1':
            orderTicket()
        elif choice == '2':
            viewRoutes()
        elif choice == '3':
            viewTrain()
        elif choice == '4':
            print("Thank you for using our program.")
            break
        else:
            print("choose is invalid. Please try again.")


mainMenu()
