#zadam rozsha cisel, pak si jedno cislo myslim v hlave a pc se snazi uhodnout cislo (vetsi/mensi nez), odpovidam a/n a pricitaji se pokusy pc, na konci se ukaze jako cislo teda uhodl a kolik pokusu mu to trvalo,to cislo hada on, ja si ho myslim pouze v hlave, tak na zaklade odpovedi a/n se bude hadat, jestli je vetsi nebo mensi nez to co si myslim, a na konci se ukaze uhodnute cislo a pocet pokusu, ktery to trvalo

import random

def main():
    print("Zadej 1 pro rozsah 1-10, 2 pro rozsah 1-50, 3 pro rozsah 1-100 a 4 pro vlastní rozsah.")

    volba = int(input("Zadej volbu: "))

    if volba == 1:
        rozsah_od = 1
        rozsah_do = 10
    elif volba == 2:
        rozsah_od = 1
        rozsah_do = 50
    elif volba == 3:
        rozsah_od = 1
        rozsah_do = 100
    elif volba == 4:
        rozsah_od = int(input("Zadej vlastní rozsah od: "))
        rozsah_do = int(input("Zadej vlastní rozsah do: "))
    else:
        print("Neplatná volba.")
        return
    
    print("")
    print(f"Mysli si číslo mezi {rozsah_od} a {rozsah_do}.")
    print("")
    print(f"k=správně, a=ano, n=ne")
    print("")
    pokusy = 0

    while True:
        hadane_cislo = random.randint(rozsah_od, rozsah_do)
        pokusy += 1
        odpoved = input(f"Je číslo větší než {hadane_cislo}? (a/n), : ").lower()

        if odpoved == 'a':
            rozsah_od = hadane_cislo + 1
        elif odpoved == 'n':
            rozsah_do = hadane_cislo - 1
        elif odpoved == 'k':
            print(f"Uhodl jsem číslo {hadane_cislo} za {pokusy} pokusů!")
            break
        else:
            print("Neplatná odpověď. Zadej 'a/A' pro ano a 'n/N' pro ne.")
            continue

        if rozsah_od > rozsah_do:
            print("Něco se pokazilo. Zkontroluj své odpovědi.")
            return

        if rozsah_od == rozsah_do:
            print(f"Uhodl jsem číslo {rozsah_od} za {pokusy} pokusů!")
            break
              

if __name__ == "__main__":
    main()
    