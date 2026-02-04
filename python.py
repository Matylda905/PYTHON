cena=int(input("Zadejte cenu knihy: "))
sleva=int(input("Zadejte slevu(%): "))
po_sleve=cena - ((cena/100)*sleva)
print(f"Původně kniha stála {cena}Kč")
print(f"Sleva byla {sleva}%")
print(f"Po sleve kniha stala {po_sleve}Kč")


