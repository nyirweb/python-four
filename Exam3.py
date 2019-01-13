# 3. Kérd be Zsófi, Kati és Juli születési évét.
# Írd ki a neveket udvariassági sorrendben (előre az idősebbeket…)!

zsofiKora = int(input("Add meg a korod Zsófi!"))
katiKora = int(input("Add meg a korod Kati!"))
juliKora = int(input("Add meg a korod Juli!"))

legidosebb = max(zsofiKora,juliKora,katiKora)
if(legidosebb==zsofiKora):
    print("Üdvözlöm Zsófi")
    if(juliKora>=katiKora):
        print("Üdvözlöm Juli!")
        print("Üdvözlöm Kati!")
    else:
        print("Üdvözlöm Kati")
        print("Üdvözlöm Juli")

if(legidosebb==katiKora):
    print("Üdvözlöm Kati!")
    if(juliKora>=zsofiKora):
        print("Üdvözlöm Juli")
        print("Üdvözlöm Zsófi")
    else:
        print("Üdvözlöm Zsófi")
        print("Üdvözlöm Juli")

if(legidosebb==juliKora):
    print("Üdvözlöm Juli!")
    if(zsofiKora>=katiKora):
        print("Üdvözlö Zsófi!")
        print("Üdvözlö Kati!")
    else:
        print("Üdvözlö Kati!")
        print("Üdvözlö Zsófi!")