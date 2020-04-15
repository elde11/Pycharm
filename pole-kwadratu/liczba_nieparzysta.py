a = input ("Podaj liczbę")
a = int(a)
b = a % 2

print(b)
if b == 0:
     print("Liczba jest liczbą parzystą")
elif b == 1:
     print("Liczba jest liczbą nieparzystą")
else:
     print("Błędne dane. Spróbuj ponownie")