#uzivatel zada rozsah, pc si zapamatuje jedno cislo a uzivatel se pomoci vetsi nez/mensi nez snazi uhodnout cislo

import random

def main():
    print("Zadej rozsah cisel od: ")
    rozsah_od = int(input())
    print("Zadej rozsah cisel do: ")
    rozsah_do = int(input())
    print("")
    pc_cislo = random.randint(rozsah_od, rozsah_do)
    print(f"Zkus uhodnout číslo mezi {rozsah_od} a {rozsah_do}.")
    pokusy = 0
    
    while True:
        uzicatel_cislo = int(input("Zadej své číslo: "))
        pokusy += 1
        print(f"Počet pokusů: {pokusy}")
        
        if uzicatel_cislo < pc_cislo:
            print("Myslím si číslo větší.")
        elif uzicatel_cislo > pc_cislo:
            print("Myslím si číslo menší.")
        else:
            print(f"Uhodl jsi číslo {pc_cislo} za {pokusy} pokusů!")
            break
        
if __name__ == "__main__":
    main()