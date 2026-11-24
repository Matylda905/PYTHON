#zadam rozsah cisel a pc hada cislo

import random

def main():
    print("Zadej rozsah cisel od: ")
    rozsah_od = int(input())
    print("Zadej rozsah cisel do: ")
    rozsah_do = int(input())
    
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