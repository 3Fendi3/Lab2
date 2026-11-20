gol = int(input("liczba goli: "))
bonus = 0

a = gol*10
if (gol>10):
    bonus = 10
elif (gol>5):
    bonus = 5

print("ilosc punktow a: " + str(a+bonus))

bonus = 0
if (gol>5):
    bonus +=5
if (gol>10):
    bonus +=10

print("ilosc punktow b: " + str(a+bonus))
