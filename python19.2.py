#zadam rozsah cisel a pc hada cislo pres min/max, at je to rychlejsi

import random

def main():
    print("Zadej rozsah cisel od: ")
    min_rozsah = int(input())
    print("Zadej rozsah cisel do: ")
    max_rozsah = int(input())
    
    print("")
    print(f"Mysli si číslo mezi {min_rozsah} a {max_rozsah}.")
    print("")
    print(f"k=správně, a=ano, n=ne")
    print("")
    pokusy = 0
    
    while True:
        hadane_cislo = (min_rozsah + max_rozsah) // 2
        pokusy += 1
        odpoved = input(f"Je číslo větší než {hadane_cislo}? (a/n), : ").lower()
        
        if odpoved == 'a':
            min_rozsah = hadane_cislo + 1
        elif odpoved == 'n':
            max_rozsah = hadane_cislo - 1
        elif odpoved == 'k':
            print(f"Uhodl jsem číslo {hadane_cislo} za {pokusy} pokusů!")
            break
        else:
            print("Neplatná odpověď. Zadej 'a/A' pro ano a 'n/N' pro ne.")
            continue
        
        if min_rozsah > max_rozsah:
            print("Něco se pokazilo. Zkontroluj své odpovědi.")
            return
        if min_rozsah == max_rozsah:
            print(f"Uhodl jsem číslo {min_rozsah} za {pokusy} pokusů!")
            break
        
if __name__ == "__main__":
    main()