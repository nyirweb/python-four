#Évszám 17-el osztható e
evSzam = int(input("Adj meg egy évszámot!"))


if(evSzam <= 0 and evSzam == 0):
    print("Hibás évszámot adtál meg az évszám nem lehet negatív szám vagy 0.")
else:
    if(evSzam%17==0):
        print("Az évszám osztható tizenhéttel!")
    else:
        print("Az évszám nem osztható tizenhéttel!")