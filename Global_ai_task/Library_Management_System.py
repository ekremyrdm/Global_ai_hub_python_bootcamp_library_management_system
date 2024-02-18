#Ekrem Yardım, Kütüphane Yönetim Sistemi
import time

class Library():
    def __init__(self):
        self.file = open("books.txt", "a+",encoding="utf-8")
    def __del__(self):
        self.file.close()

    def list_Books(self):
        self.file.seek(0)
        liste=self.file.read()
        liste=liste.splitlines()
        if len(liste)==0:
            print("The library is empty")
            time.sleep(1)
        else:
            for x in liste:
                liste=x.split(",")
                adı,yazarı=liste[:2]#sadece yazar adı ve kitabın adı istendiği için ilk iki inexteki bilgileri almaya çalıştım
                print("Book:{}, Author:{}".format(adı,yazarı))

        time.sleep(2)
    def add_book(self):
        adı=input("Please enter the title of the book.\n")
        yazarı=input("Please enter the name of author\n")
        yayınlanma_yılı=input("Please enter the publication year\n")
        sayfa_sayısı=input("Please enter the number of pages\n")
        eklenecek=adı+","+yazarı+","+yayınlanma_yılı+","+sayfa_sayısı+"\n"
        self.file.write(eklenecek)
        print("The book is being added to the library...")
        time.sleep(2)
        print("The book has been added to the library")
        time.sleep(1)

    def remove_book(self):
        adı=input("Enter the book title to remove ")
        self.file.seek(0)
        liste=self.file.read()
        liste=liste.splitlines()
        kitap_adları=[]
        kontrol=0
        for i in liste:
            kitap_adı=i.split(",")[0]
            kitap_adları.append(kitap_adı)
        for i in kitap_adları:
            if adı == i:
                kontrol=1
                kitabın_sırası=kitap_adları.index(i)
                del liste[kitabın_sırası]
                print("The book named {} is Deleted".format(adı))
            else:
                pass
        if kontrol == 0:
            print("The book to be deleted was not found in the library")
            time.sleep(1)
        else:
            pass

        self.file.seek(0)
        self.file.truncate()
        for kitap in liste:
            self.file.write(kitap+"\n")


lib=Library()

while True:
    print("""
    Welcome to the Library Management System
    *** MENU***
    1) List Books
    2) Add Book
    3) Remove Book
    ***** Enter "q" to exit the program *****
    """)
    işlem = input("Enter your choice:")
    if (işlem == "q"):
        print("Program shutting down...")
        break

    elif (işlem == "1"):
        lib.list_Books()
    elif (işlem == "2"):
        lib.add_book()
    elif (işlem == "3"):
        lib.remove_book()
    else:
        print("Invalid input, please try again")
        time.sleep(1)