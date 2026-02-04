heslo=(input("Zadej heslo: "))

if(len(heslo) >= 8):
    print("heslo je pouzitelne")
else:
    print("heslo je nepouzitelne")

heslo2=(input("Zadej heslo znovu: "))

if(len(heslo2) >= 8):
    print("heslo je pouzitelne")
else:
    print("heslo je nepouzitelne")

if(heslo == heslo2):
    print("shoda")
else:
    print("heslo se neshoduje!")

