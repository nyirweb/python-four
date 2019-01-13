# Kérj be egy egész óra értéket. Ha a szám nem 0 és 24 óra között van,
# akkor adjon hibaüzenetet, egyébként köszönjön el a program a napszaknak megfelelően!
# 4-9: Jó reggelt!, 10-17: Jó napot!, 18-21: Jó estét!, 22-3: Jó éjszakát!

ido = int(input("Add meg az időt!"))
elkoszones = ["Jó reggelt!","Jó napot!","Jó estét!","Jó éjszakát!"]

if(ido >= 0 and ido <=24):
    if(ido>=4 and ido<=9):
        print(elkoszones[0])

    if(ido>=10 and ido<=17):
        print(elkoszones[1])

    if(ido>=18 and ido<=21):
        print(elkoszones[2])

    if(ido>=22):
        print(elkoszones[3])
    if(ido<=3):
        print(elkoszones[3])
else:
    print("Sajnos nem egész óra értéket adtál meg!")