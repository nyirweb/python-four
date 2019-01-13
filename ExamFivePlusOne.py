# 5+1. Egy dolgozatra annak pontszámától függően a következő osztályzatot adják:
# elégtelen (1): 0 – 29 elégséges (2): 30 – 37 közepes (3): 38 – 43 jó (4): 44 – 49 jeles (5): 50 – 55
# Kérje be a dolgozat pontszámát, majd írja ki az osztályzatot számmal és betűvel!

osztalyzatok = ["Elégtelen (1)","Elégséges (2)","Közepes (3)","Jó (4)","Jeles (5)"]
pontSzam = int(input("Add meg a dolgozaton elért eredményed! (0 és 55 pont között lehetséges)"))


if(pontSzam >= 0 and pontSzam <= 55):
    for j in range (0,30):
        if(pontSzam==j):
            print("\nAz elért eredmény: ",osztalyzatok[0])

    for k in range (30,38):
        if(pontSzam == k):
            print("\nAz elért eredmény: ",osztalyzatok[1])

    # egy L, mint László betű nem pedig 1-es (Egyes) szám!
    for l in range (38,44):
        if(pontSzam == l):
            print("\nAz elért eredmény: ",osztalyzatok[2])
    for m in range (44,50):
        if(pontSzam == m):
            print("\nAz elért eredmény: ",osztalyzatok[3])
    for n in range (50,56):
        if(pontSzam == n):
            print("\nAz elért eredmény: ",osztalyzatok[4])
else:
    print("Az elért pontszámoknak 0 és 55 közé kell esnie!")