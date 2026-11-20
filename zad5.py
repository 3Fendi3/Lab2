
plik = open("notowania_gieldowe.txt", "r")
print(plik.read())
plik.close()

with open("notowania_gieldowe.txt", "a") as plik:
    plik.write("\nALR, 113")
    plik.close()

a = open("notowania_gieldowe.txt", "r")
print(a.read())
a.close()
