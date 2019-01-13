# Kérj be egy egyjegyű, nem negatív számot! Írd ki a szám szöveges formáját (1=egy, 2=kettő stb.)

szam = int(input("Adj meg egy nem negatív számot 1 és 9 között!"))

lista = ["Egy","Kettő","Három","Négy","Öt","Hat","Hét","Nyolc","Kilenc"]

if(szam<=9 and szam>=1):
    for i in range(0,9):
        index = szam-1
        if(i==index):
            print(lista[i])
else:
    print("Nem jó számot adtál meg! A számnak 1 és 9 közé kell esnie!")