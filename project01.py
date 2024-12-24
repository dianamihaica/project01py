def solicita_nume_prenume():
    while True:
        nume_complet = input("Introduceți numele și prenumele utilizatorului: ").strip()
        if len(nume_complet.split()) >= 2:
            nume, prenume = nume_complet.split(maxsplit=1)
            return nume, prenume
        else:
            print("Numele nu a fost introdus corect. Asigurați-vă că introduceți cel puțin două cuvinte.")

def solicita_suma_achizitii():
    while True:
        try:
            nr_achizitii = int(input("Introduceți numărul total de achiziții efectuate în ultimul an: "))
            if nr_achizitii < 0:
                raise ValueError("Numărul de achiziții nu poate fi negativ.")
            achizitii = []
            for i in range(nr_achizitii):
                while True:
                    try:
                        suma = float(input(f"Introduceți suma pentru achiziția {i + 1}: "))
                        if suma < 0:
                            raise ValueError("Suma nu poate fi negativă.")
                        achizitii.append(suma)
                        break
                    except ValueError as e:
                        print(e)
            return achizitii
        except ValueError:
            print("Introduceți un număr valid.")

def calculeaza_statut(achizitii):
    suma_totala = sum(achizitii)
    achizitii_peste_10000 = len([suma for suma in achizitii if suma > 10000])
    
    if suma_totala > 100000 and len(achizitii) > 10:
        statut = "VIP"
        reducere = 0.10
    else:
        statut = "STANDARD"
        reducere = 0.05
    
    return statut, reducere, suma_totala, achizitii_peste_10000

def calculeaza_pret_reducere(reducere):
    while True:
        try:
            pret_articol = float(input("Introduceți prețul articolului pe care doriți să-l cumpărați: "))
            if pret_articol < 0:
                raise ValueError("Prețul articolului nu poate fi negativ.")
            pret_final = pret_articol * (1 - reducere)
            return pret_final
        except ValueError as e:
            print(e)

def main():
    print("--- Gestionarea clienților pentru platforma de vânzări online ---")
    nume, prenume = solicita_nume_prenume()
    
    print(f"Bun venit, {nume} {prenume}!")
    achizitii = solicita_suma_achizitii()
    
    statut, reducere, suma_totala, achizitii_peste_10000 = calculeaza_statut(achizitii)
    
    print("\nRezumatul achizițiilor:")
    print(f"Suma totală cheltuită: {suma_totala:.2f} lei")
    print(f"Numărul achizițiilor peste 10.000 lei: {achizitii_peste_10000}")
    print(f"Statut atribuit: {statut}")
    print(f"Reducerea aprobată pentru următoarele achiziții: {reducere * 100}%")
    
    pret_final = calculeaza_pret_reducere(reducere)
    print(f"Prețul cu reducere pentru articolul ales este: {pret_final:.2f} lei")

if __name__ == "__main__":
    main()
