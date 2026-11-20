a = int(input("Podaj liczbe a: "))
b = int(input("Podaj liczbe b: "))
c = int(input("Podaj liczbe c: "))

if a > b:
    x = a
    a = b
    b = x

if a > c:
    x = a
    a = c
    c = x
if b > c:
    x = b
    b = c
    c = x

print(a, b, c)
