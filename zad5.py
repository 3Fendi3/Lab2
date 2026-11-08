
plik = open("gielda.txt", "r")
#print(plik.read())
plik.close()

with open("gielda.txt", "a") as plik:
    plik.write("\nalr, 113")
    plik.close()

a = open("gielda.txt", "r")
print(a.read())
a.close()

