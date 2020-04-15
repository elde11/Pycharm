m = input("Podaj rodzaj figury")

if  m =="kwadrat" or m == "Kwadrat":
        a = input("Podaj długość boku kwadratu a=")
        a = float(a)
        x = input("Podaj rodzaj operacji (pole czy obwód)")
        if  x == "pole" or x ==  "Pole":
            print("Pole kwadratu =", a**2)
        elif x == "obwód" or x == "Obwód" or x == "obwod" or x =="Obwod":
            print("Pole kwadratu =", 4*a)
        else:
            print ("Nieznana operacja")

elif m == "prostokąt" or m == "Prostokąt" or m == "prostokat" or m == "Prostokat":
        a = input("Podaj długość pierwszego boku prostokąta a=")
        a = float(a)
        b = input("Podaj długość drugiego boku prostokąta b=")
        b = float(b)
        x = input("Podaj rodzaj operacji (pole czy obwód)")
        if x == "Pole" or x == "pole":
            print("Pole prostokąta =", a*b)
        elif x == "obwód" or x == "Obwód" or x == "obwod" or x == "Obwod":
            print("Obwód prostokąta =", 2*a+2*b)
        else:
            print ("Nieznana operacja")

elif m == "Koło" or m == "koło" or m == "Kolo" or m == "kolo":
        r = input("Podaj promień koła r=")
        r = float(r)
        x = input("Podaj rodzaj operacji (pole czy obwód)")
        if x == "pole" or x == "Pole":
            print("Pole koła =", 3.14*r**2)
        elif x == "obwód" or x == "Obwód" or x == "obwod" or x == "Obwod":
            print("Obwód koła =", 2*3.14*r)
        else:
            print ("Nieznana operacja")

else:
    print("Nieznana figura")