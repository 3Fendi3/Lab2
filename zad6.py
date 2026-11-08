a = str(input("wpisz jedna duza lub maja litere: "),)
if a.isalpha():
    if (len(a)>1):
        print("miales wpisac jedna litere!!!!!!")
    else:
        if (a.islower()):
            print("litera jest mala")
        else:
            print("litera jest duza")
else:
    print("wpisz normalna litere")