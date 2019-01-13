# Hordó bor, befér nem fér
# Van egy henger alakú hordónk,
# melybe nem tudjuk, hogy belefér-e a rendelkezésre álló bor.
# Kérd be a bor mennyiségét literben, majd a hordó
# összes szükséges adatát cmben. Adj tájékoztatást,
# hogy hány literes a hordó, és hogy belefér-e a hordóba a bor!
# Ha belefér, akkor add meg, hogy mennyi férne még bele!
# Írd ki százalékosan is a telítettséget! Az adatokat egészre kerekítve írd ki!

pi = 3.14
borL = float(input("Add meg a bor mennyiségét (literben)!"))
d = float(input("Add meg a hordó átmérőjét (centiméterben)!"))
r = float(d/2)
m = float(input("Add meg a hordó magasságát (centiméterben)!"))

hordoV = float(pi*(r**2)*m)
hordoL = float(hordoV*0.001)
telitettsegSzamol = float((hordoL/borL)*float(100))

print(telitettsegSzamol)
if(borL != hordoL):
    if(borL > hordoL):
        print("A hordó kapacitása:",float(hordoL),"(liter) Ezért nem fér bele a hordóba a bor!")
        print("A hordóba a bor",float(telitettsegSzamol),"százaléka fér bele!")
    else:
        print("A hordó kapacitása:", float(hordoL), "(liter) Ezért fér bele a hordóba a bor!")
        print("A hordóba még", float(hordoL-borL), "(liter) bor fér bele",
              "A hordó ",round(float(telitettsegSzamol)/float(100),3),"%-a telt meg!")
else:
    print("A hordó kapacitása:", round(hordoL), "(liter) Ez megegyezol a bor mennyiségével!")
    print("A hordóba pontosan", round(hordoL), "(liter) bor fér bele",
          "A hordóba egy cseppel több bor sem fér! 100 százaléka tele van!")
