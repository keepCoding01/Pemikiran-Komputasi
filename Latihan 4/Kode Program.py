# ALGORITMA
# A. MULAI
# B. PANGGIL LIBRARY PYTHON YAITU TABULATE, GUNA UNTUK MEMBUAT TABEL
# C. INISIALISASI VARIABEL MAHASISWA DENGAN LIST KOSONG
# D. INISIALISASI FUNGSI ADDSTUDENTDATA UNTUK MENAMBAHKAN DATA
# 	- PANGGIL VARIABEL MAHASISWA KE DALAM FUNGSI INI
# 	- CETAK GARIS PEMBATAS DAN JUDUL
# 	- LAKUKAN INPUTAN MULAI DARI NIM, NAMA, TEMPAT DAN TANGGAL LAHIR, JURUSAN DAN TANGGAL MASUK
# 	- TAMBAHKAN SELURUH DATA INPUTAN KE DALAM VARIABEL MAHASISWA
# 	- CETAK PEMBERITAHUAN BAHWA DATA TELAH BERHASIL DITAMBAHKAN
# E. INISIALISASI FUNGSI SHOWSTUDENTDATA
# 	- PANGGIL VARIABEL MAHASISWA KE DALAM FUNGSI INI
# 	- JIKA MAHASISWA TIDAK ADA, CETAK TIDAK ADA DATA MAHASISWA
# 	- CETAK GARIS PEMBATAS DATA MAHASISWA DAN JUDULNYA
# 	- INISIALISASI TEMPAT UNTUK MENAMPUNG KESELURUHAN DATA DIDALAM LIST
# 	- LAKUKAN PERULANGAN INDEX DENGAN DATA YANG ADA
# 	- TAMBAHKAN DATANYA KE MASING-MASING FORMAT
# 	- CETAK DATA MAHASISWA DENGAN TABEL DARI LIBRARY TABULATE
# F. INISIALISASI FUNGSI CHANGESTUDENTDATA UNTUK MENGUBAH DATA
# 	- PANGGIL VARIABEL MAHASISWA KE DALAM FUNGSI INI
# 	- INPUT NIM MAHASISWA
# 	- LAKUKAN PERULANGAN INDEX DENGAN DATA YANG ADA
# 	- JIKA NIM YANG DIINPUT == NIM YANG ADA DI DATA, MAKA TAMBAHKAN DATA SESUAI FORMAT
# 	- CETAK DATA DENGAN TABEL MENGGUNAKAN LIBRARY TABULATE
# 	- LAKUKAN PERULANGAN WHILE SELAMA KONDISINYA BENAR
# 	- CETAK GARIS PEMBATAS DAN JUDUL
# 	- INISIALISASI VARIABEL DATAQUESTION = 0
# 	- LAKUKAN PERTANYAAN MENGENAI DATA YANG INGIN DI UBAH DENGAN PERKONDISIAN
# 	- JIKA PENGGUNA MENGINPUTNYA DATA TERBARU, MAKA SETTING DATAQUESTION MENJADI TRUE UNTUK MENYIMPAN DATANYA
# 	- JIKA SUDAH SELESAI MAKA CETAK PEMBERITAHUAN BAHWA DATA TELAH DI UBAH
# 	- APABILA PENGGUNA TIDAK MENGINPUT DATA TERBARU, CETAK PEMBERITAHUANNYA
# 	- JIKA NIM YANG DI INPUT TIDAK SAMA DENGAN NIM YANG ADA DI DATA, MAKA CETAK PEMBERITAHUAN MAAF, NIM TERSEBUT TIDAK DITEMUKAN DI DATA MAHASISWA
# G. INISIALISASI FUNGSI SORTSTUDENTDATA UNTUK MENGURUTKAN DATA
# 	- PANGGIL VARIABEL MAHASISWA KE DALAM FUNGSI INI
# 	- LAKUKAN PERULANGAN WHILE SELAMA KONDISI BENAR
# 	- CETAK GARIS PEMBATAS DAN JUDUL
# 	- CETAK MENU PILIHAN PENGURUTAN UNTUK PENGGUNA
# 	- LAKUKAN INPUT NILAI ATAS PILIHAN PENGGUNA
# 	- JIKA INPUTAN == 1, MAKA DATA AKAN DIURUTKAN BERDASARKAN NIM
# 	- JIKA INPUTAN == 2, MAKA DATA AKAN DIURUTKAN BERDASARKAN NAMA
# 	- JIKA INPUTAN == 3, MAKA DATA AKAN DIURUTKAN BERDASARKAN JURUSAN
# 	- JIKA INPUTAN == 4, MAKA DATA AKAN DIURUTKAN BERDASARKAN TAHUN MASUK
# 	- JIKA INPUTAN == 5, MAKA AKAN KELUAR KE MENU UTAMA
# 	- JIKA TIDAK SEMUANYA, MAKA CETAK INVALID!
# 	- INISIALISASI FUNGSI MERGESORT DENGAN PARAMETER N DAN PROSES
# 	- JIKA PANJANG DATA N KURANG DARI 1, RETURN/KEMBALIKAN NILAI N
# 	- PROSES PERTAMA IALAH MEMBAGI DUA DATA LEWAT VARIABEL MID PROSES
# 	- PROSES KEDUA IALAH MENGURUTKAN DATA DARI SISI KIRI
# 	- PROSES KETIGA IALAH MENGURUTKAN DATA DARI SISI KANAN
# 	- RETURN/KEMBALIKAN NILAI MERGE KIRI, KANAN, DAN PROSESNYA
# 	- INISIALISASI FUNGSI MERGE DENGAN PARAMETER LEFTPROSES, RIGHTPROSES, BAGIAN
# 	- INISIALISASI VARIABEL MAHASISWA DENGAN LIST KOSONG
# 	- INISIALISASI NILAI I DAN J = 0
# 	- LAKUKAN PERULANGAN I JIKA LEBIH KECIL DARI PANJANG PROSES BAGIAN KIRI DAN J LEBIH KECIL DARI PROSES BAGIAN KANAN
# 	- JIKA INDEKS DARI PROSES KIRI LEBIH KECIL DARI YANG KANAN, TAMBAHKAN NILAINYA KE VARIABEL MAHASISWA. LANJUT KE NODE BERIKUTNYA
# 	- JIKA TIDAK, MAKA TAMBAHKAN NILAI DARI PROSES KANAN KE VARIABEL MAHASISWA. LANJUT KE NODE BERIKUTNYA
# 	- KESELURUHAN DATA INDEKS BAGIANM KIRI DAN KANAN DIMASUKKAN KE DALAM LIST MAHASISWA. RETURN/KEMBALIKAN NILAI
# 	- PANGGIL KEMBALI FUNGSI MERGE SORT DENGAN ARGUMEN MAHASISWA DAN PROSES
# 	- CETAK PEMBERITAHUAN BAHWA DATA TELAH DIURUTKAN
# 	- TAMPILKAN DATANYA DAN ULANGI FUNGSI SORTSTUDENTDATA
# H. INISIALISASI FUNGSI FINDIDSTUDENT DENGAN PARAMETER SEARCHIDSTUDENT
# 	- PANGGIL VARIABEL MAHASISWA KE DALAM FUNGSI INI
# 	- INISIALISASI LIST SEACRHRESULT KOSONG
# 	- LAKUKAN PERULANGAN INDEX DENGAN DATA
# 	- JIKA SEARCHIDSTUDENT ADA DI DATA NIM, TAMBAHKAN NILAINYA KE SEARCHRESULT. RETURN/KEMBALIKAN NILAI
# I. INISIALISASI FUNGSI FINDNAMESTUDENT DENGAN PARAMETER SEARCHNAMESTUDENT
# 	- PANGGIL VARIABEL MAHASISWA KE DALAM FUNGSI INI
# 	- INISIALISASI LIST SEACRHRESULT KOSONG
# 	- LAKUKAN PERULANGAN INDEX DENGAN DATA
# 	- JIKA SEARCHNAMESTUDENT ADA DI DATA NAMA, TAMBAHKAN NILAINYA KE SEARCHRESULT. RETURN/KEMBALIKAN NILAI
# J. INISIALISASI FUNGSI SEARCHFORSTUDENTDATA
# 	- LAKUKAN PERULANGAN WHILE SELAMA KONDISI BENAR
# 	- CETAK PILIHAN UNTUK PENGGUNA
# 	- LAKUKAN INPUTAN UNTUK MEMILIH TIPE PENCARIAN
# 	- JIKA PILIHANNYA == 1, MAKA PENGGUNA HARUS MENGINPUTKAN KATA KUNCI YANG INGIN DICARI. KEMUDIAN PANGGIL FUNGSI FINDIDSTUDENT DAN CETAK DATA DITEMUKAN. KELUAR DARI PERULANGAN
# 	- JIKA PILIHANNYA == 2, MAKA PENGGUNA HARUS MENGINPUTKAN KATA KUNCI YANG INGIN DICARI. JALANKAN FUNGSI FINDNAMESTUDENT DAN KELUAR DARI PERULANGAN.
# 	- JIKA TIDAK KEDUANYA, CETAK PEMBERITAHUAN INVALID!
# 	- LAKUKAN PENGKONDISIAN UNTUK SEARCHRESULT
# 	- CETAK PEMBERITAHUAN BERIKUT DATA YANG DICARI
# 	- INISIALISASI VARIABEL ALLDATASTUDENTS DENGAN LIST KOSONG
# 	- LAKUKAN PERULANGAN INDEX DENGAN DATA YANG ADA DI SEARCHRESULT
# 	- TAMBAHKAN DATANYA KE VARIABEL ALLDATASTUDENTS SESUAI FORMAT KEMUDIAN CETAK DENGAN TABEL
# 	- JIKA DATANYA TIDAK ADA, MAKA CETAK PEMBERITAHUAN BAHWA DATA YANG DICARI TIDAK DITEMUKAN
# K. INISALISASI FUNGSI MAIN
# 	- PANGGIL VARIABEL MAHASISWA KE DALAM FUNGSI INI
# 	- LAKUKAN PERULANGAN SELAMA KONDISI BENAR
# 	- CETAK GARIS PEMBATAS DAN JUDUL
# 	- CETAK MENU PILIHAN PENGGUNA
# 	- LAKUKAN INPUTAN ATAS PILIHAN YANG ADA DI MENU
# 	- JIKA PILIHAN == 1, MAKA JALANKAN FUNGSI ADDSTUDENTDATA
# 	- JIKA PILIHAN == 2, MAKA JALANKAN FUNGSI SHOWSTUDENTDATA
# 	- JIKA PILIHAN == 3, MAKA JALANKAN FUNGSI CHANGESTUDENTDATA
# 	- JIKA PILIHAN == 4, MAKA JALANKAN FUNGSI SORTSTUDENTDATA
# 	- JIKA PILIHAN == 5, MAKA JALANKAN FUNGSI SEARCHFORSTUDENTDATA
# 	- JIKA PILIHAN == 6, MAKA CETAK TERIMA KASIH SUDAH MENGGUNAKAN PROGRAM KELOMPOK KAMI
# 	- JIKA PILIHAN TIDAK SEMUANYA, MAKA CETAK PEMBERITAHUAN INVALID!
# L. PANGGIL FUNGSI MAIN.
# M. SELESAI

# KOMPLEKSITAS WAKTU :
# - ADDSTUDENTDATA --> O(1) // KONSTAN
# - SHOWSTUDENTDATA --> O(n) // LANJAR
# - CHANGESTUDENTDATA --> O(n) // LANJAR
# - SORTSTUDENTDATA --> O(n log n)
# - FINDIDSTUDENT --> O(n) // LANJAR
# - FINDNAMESTUDENT --> O(n) // LANJAR
# - SEARCHFORSTUDENTDATA --> O(n) // LANJAR
#   TOTAL KESELURUHAN   = O(n log n)

# KOMPLEKSITAS RUANG :
# - ADDSTUDENTDATA --> O(1) // KONSTAN
# - SHOWSTUDENTDATA --> O(n) // LANJAR
# - CHANGESTUDENTDATA --> O(1) // KONSTAN
# - SORTSTUDENTDATA --> O(n) // LANJAR
# - FINDIDSTUDENT --> O(n) // LANJAR
# - FINDNAMESTUDENT --> O(n) // LANJAR
# - SEARCHFORSTUDENTDATA --> O(n) // LANJAR-
#   TOTAL KESELURUHAN  = O(n)

from tabulate import tabulate
students = []


def addStudentsData():
    global students
    print("="*70)
    print("\t\t\t Add Student Data")
    print("="*70)
    studentNIM = input("Input ID Students\t\t\t: ")
    studentName = input("Input Name\t\t\t\t: ")
    studentPlaceOfBirth = input("Input Place of Birth\t\t\t: ")
    studentDateOfBirth = input("Input Date of Birth (dd/mm/yyyy)\t: ")
    studentMajor = input("Input Major\t\t\t\t: ")
    studentEntryYear = input("Input Entry Year\t\t\t: ")
    students.append({
        "ID STUDENT": studentNIM,
        "NAME": studentName,
        "PLACE of BIRTH": studentPlaceOfBirth,
        "DATE of BIRTH": studentDateOfBirth,
        "MAJORITY": studentMajor,
        "ENTRY YEAR": studentEntryYear
    })
    print("\nStudent data added successfully!")


def showStudentData():
    global students
    if not students:
        print("\nThere is no student data")
        return
    print("\n=====================================================================")
    print("\t\t\tStudent Data:")
    print("=====================================================================")
    allDataStudents = []
    for index in students:
        allDataStudents.append(
            [index["ID STUDENT"], index["NAME"], index["MAJORITY"], index["ENTRY YEAR"]])
    print(tabulate(allDataStudents, headers=[
          "ID STUDENT", "NAME", "MAJORITY", "ENTRY YEAR"], tablefmt="grid"))


def changeStudentData():
    global students
    studentNIM = input("The student's ID will be changed: ")
    for index in students:
        if index["ID STUDENT"] == studentNIM:
            print("\nFollowing are the student data : ")
            allDataStudents = [
                {"FIELD": "ID STUDENT", "DETAIL": index["ID STUDENT"]},
                {"FIELD": "NAME", "DETAIL": index["NAME"]},
                {"FIELD": "PLACE of BIRTH", "DETAIL": index["PLACE of BIRTH"]},
                {"FIELD": "DATE of BIRTH", "DETAIL": index["DATE of BIRTH"]},
                {"FIELD": "MAJORITY", "DETAIL": index["MAJORITY"]},
                {"FIELD": "ENTRY YEAR", "DETAIL": index["ENTRY YEAR"]}
            ]
            print(tabulate(allDataStudents, headers="keys", tablefmt="grid"))

            while True:
                print(
                    "\n=====================================================================")
                print("\t\t\t Latest Student Data")
                print(
                    "=====================================================================")
                changeName = input("Change Name (y/t)\t\t\t: ")
                dataQuestion = 0
                if changeName.lower() == "y":
                    index["NAME"] = input("Enter a new Name\t\t\t: ")
                    dataQuestion = True
                elif changeName.lower() == "t":
                    pass
                else:
                    print("Invalid choice! Please enter 'y' or 't'.")
                    changeName = input("Change Name (y/t)\t\t\t: ")
                    if changeName.lower() == "y":
                        index["NAME"] = input("Enter a new Name\t\t\t: ")
                        dataQuestion = True
                    elif changeName.lower() == "t":
                        pass

                changePlaceOfBirth = input("Change Place of Birth (y/t)\t\t: ")
                if changePlaceOfBirth.lower() == "y":
                    index["PLACE of BIRTH"] = input(
                        "Enter the new Place of Birth\t\t: ")
                    dataQuestion = True
                elif changePlaceOfBirth.lower() == "t":
                    pass
                else:
                    print("Invalid choice! Please enter 'y' or 't'.")
                    changePlaceOfBirth = input(
                        "Change Place of Birth (y/t)\t\t: ")
                    if changePlaceOfBirth.lower() == "y":
                        index["PLACE of BIRTH"] = input(
                            "Enter the new Place of Birth\t\t: ")
                        dataQuestion = True
                    elif changePlaceOfBirth.lower() == "t":
                        pass

                changeDateOfBirth = input("Change Date of Birth (y/t)\t\t: ")
                if changeDateOfBirth.lower() == "y":
                    index["DATE of BIRTH"] = input(
                        "Enter new Date of Birth\t\t\t: ")
                    dataQuestion = True
                elif changeDateOfBirth.lower() == "t":
                    pass
                else:
                    print("Invalid choice! Please enter 'y' or 't'.")
                    changeDateOfBirth = input(
                        "Change Date of Birth (y/t)\t\t: ")
                    if changeDateOfBirth.lower() == "y":
                        index["DATE of BIRTH"] = input(
                            "Enter new Date of Birth\t\t\t: ")
                        dataQuestion = True
                    elif changeDateOfBirth.lower() == "t":
                        pass

                changeMajor = input("Change Majority (y/t)\t\t\t: ")
                if changeMajor.lower() == "y":
                    index["MAJORITY"] = input(
                        "Enter new Majority\t\t\t: ")
                    dataQuestion = True
                elif changeMajor.lower() == "t":
                    pass
                else:
                    print("Invalid choice! Please enter 'y' or 't'.")
                    changeMajor = input(
                        "Change Majority (y/t)\t\t\t: ")
                    if changeMajor.lower() == "y":
                        index["MAJORITY"] = input(
                            "Enter new Majority\t\t\t: ")
                        dataQuestion = True
                    elif changeMajor.lower() == "t":
                        pass

                changeYearIn = input("Change Entry Year (y/t)\t\t\t: ")
                if changeYearIn.lower() == "y":
                    index["ENTRY YEAR"] = input(
                        "Enter the new Entry Year\t\t: ")
                    dataQuestion = True
                    break
                elif changeYearIn.lower() == "t":
                    break
                else:
                    print("Invalid choice! Please enter 'y' or 't'.")
                    changeYearIn = input("Change Entry Year (y/t)\t\t\t: ")
                    if changeYearIn.lower() == "y":
                        index["ENTRY YEAR"] = input(
                            "Enter the new Entry Year\t\t: ")
                        dataQuestion = True
                        break
                    elif changeYearIn.lower() == "t":
                        break

            if dataQuestion:
                print(f"Data with ID {
                      studentNIM} has been successfully changed .")
            else:
                print("No Data Changed")
            return
    if ["ID STUDENT"] != studentNIM:
        print(f"Sorry, ID {studentNIM} was not found.")

# Merge Sort


def sortStudentData():
    global students

    while True:
        print("\n=====================================================================")
        print("\t\t\t Sort Student Data")
        print("=====================================================================")
        print("1. ID Students")
        print("2. Name")
        print("3. Majority")
        print("4. Entry Year")
        print("5. Close")
        print("=====================================================================")

        to = int(input("Sort type (Number Input): "))

        if to == 1:
            process = "ID STUDENT"
            break
        elif to == 2:
            process = "NAME"
            break
        elif to == 3:
            process = "MAJORITY"
            break
        elif to == 4:
            process = "ENTRY YEAR"
            break
        elif to == 5:
            return
        else:
            print("INVALID!")

    def mergeSort(n, process):
        if len(n) <= 1:
            return n

        midProcess = len(n) // 2
        leftProcess = mergeSort(n[:midProcess], process)
        rightProcess = mergeSort(n[midProcess:], process)

        return merge(leftProcess, rightProcess, process)

    def merge(leftProcess, rightProcess, bagian):
        students = []
        i = 0
        j = 0
        while i < len(leftProcess) and j < len(rightProcess):
            if leftProcess[i][bagian] <= rightProcess[j][bagian]:
                students.append(leftProcess[i])
                i += 1
            else:
                students.append(rightProcess[j])
                j += 1

        students += leftProcess[i:]
        students += rightProcess[j:]

        return students

    students = mergeSort(students, process)
    print("Succeed! The data has been sorted accordingly ", process)
    showStudentData()
    sortStudentData()


def findIDStudent(searchIDStudent):
    global students
    searchResult = []
    for index in students:
        if searchIDStudent in index["ID STUDENT"]:
            searchResult.append(index)
    return searchResult


def findNameStudent(searchNameStudent):
    global students
    searchResult = []
    for index in students:
        if searchNameStudent.lower() in index["NAME"].lower():
            searchResult.append(index)
    return searchResult

# Linear Search


def searchForStudentData():
    while True:
        print("Select a section to search:")
        print("1. Student ID")
        print("2. Student Name")
        to = int(input("Search Type(Enter number): "))
        if to == 1:
            searchIDStudent = input(
                "Enter the keywords you are looking for : ")
            searchResult = findIDStudent(searchIDStudent)
            print("Search complete.")
            break
        elif to == 2:
            searchNameStudent = input(
                "Enter the keywords you are looking for : ")
            searchResult = findNameStudent(searchNameStudent)
            break
        else:
            print("INVALID!")

    if searchResult:
        print("\nSucceed! Here's the data:")
        allDataStudents = []
        for index in searchResult:
            allDataStudents.append([index["ID STUDENT"], index["NAME"],  index["PLACE of BIRTH"],
                                    index["DATE of BIRTH"], index["MAJORITY"], index["ENTRY YEAR"]])
        print(tabulate(allDataStudents, headers=[
              "NO", "ID STUDENT", "NAME", "PLACE of BIRTH", "DATE of BIRTH", "MAJORITY", "ENTRY YEAR"], tablefmt="grid"))
    else:
        print("Your search results were not found!")


def main():
    global students
    while True:
        print("\n=====================================================================")
        print("\t\t\tStudent Data Application")
        print("=====================================================================")
        print("1. Add Student Data")
        print("2. Show Student Data")
        print("3. Change Student Data")
        print("4. Sort Student Data")
        print("5. Search for Student Data")
        print("6. Close")
        print("=====================================================================")
        to = int(input("Enter to (1 - 6): "))
        if to == 1:
            addStudentsData()
        elif to == 2:
            showStudentData()
        elif to == 3:
            changeStudentData()
        elif to == 4:
            sortStudentData()
        elif to == 5:
            searchForStudentData()
        elif to == 6:
            print(
                "Thank you for using our group program")
            break
        else:
            print("INVALID!")


main()
