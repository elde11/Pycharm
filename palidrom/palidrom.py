slowo = input("Wpisz slowo: ")
czy_palindrom = True  # lub False

for i in range(len(slowo)):
    if slowo[i] != slowo[-i - 1]:
        czy_palindrom = False
        break

print(f"Palindrom: {czy_palindrom}")  # "Palindrom: " + str(czy_palindrom)
if czy_palindrom:
    print("TAK to jest palindrom")
else:
    print("Niestety to nie jest palindrom")