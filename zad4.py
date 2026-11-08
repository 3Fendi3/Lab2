gol = int(input("liczba goli: "))
bonus = 10


a = gol*bonus
if (gol>5):
    bonus +=5
if (gol>10):
    bonus +=10

print("ilosc punktow: " + str(bonus))


