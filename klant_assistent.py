import json

geldige_klanttypes = ["nieuw", "bestaand", "premium"]

def verwerk_klanten():
    klanten = []

    # blijf de vraag opnieuw stellen totdat de gebruiker een heel getal groter dan 0 invoert.
    while True:
        try:
            aantalKlanten = int(input("Hoeveel klanten wilt u invullen? "))
            if aantalKlanten > 0:
                break
            print("Het aantal moet groter zijn dan 0.")
        except ValueError:
            print("Voer een geldig geheel getal in.")

    for i in range(aantalKlanten):
        klant = verzamel_klant(i + 1)
        klanten.append(klant)

        advies = genereer_advies(klant)
        klant["advies"] = advies
        print("Advies:", advies)
        print()

    
    return klanten


def verzamel_klant(klantNummer):
    print("klant nummer:", klantNummer)

    naam = str(input("Wat is de naam van deze klant? "))
    # blijf de leeftijd vragen totdat de gebruiker een legitiem getal invoert
    while True:
        try:
            leeftijd = int(input("Wat is de leeftijd van deze klant? "))
            if leeftijd >= 0:
                break
            print("Leeftijd kan niet negatief zijn.")
        except ValueError:
            print("Voer een geldig geheel getal in.")    

    # blijf het bestedingsniveau vragen totdat de gebruiker een legitiem getal invoert
    while True:
        try:
            besteding = float(input("Wat is het bestedingsniveau van deze klant? "))
            if besteding >= 0:
                break
            print("Besteding kan niet negatief zijn.")
        except ValueError:
            print("Voer een geldig bedrag in (bijvoorbeeld 100 of 99.95).")

    # check of de klant een van de 3 geldige opties als klanttype invoert
    while True:
        klanttype = input(
            "Wat is het klanttype van deze klant? (nieuw/bestaand/premium) "
        ).lower()

        if klanttype in geldige_klanttypes:
            break
        else:
            print("Ongeldig klanttype. Kies uit: nieuw, bestaand of premium.")

    
    klant = {
        "naam": naam,
        "leeftijd": leeftijd,
        "besteding": besteding,
        "klanttype": klanttype,
        "advies": None
    }

    return klant



def genereer_advies(klant): 
    advies = ""

    if (klant["klanttype"] == "premium"):
        advies = "Intensievere begeleiding (complex dossier)"
    elif (klant["leeftijd"] >= 67):
        advies = "AOW-check en extra begeleiding"
    elif (klant["besteding"] > 100):
        advies = "Check aanvullende regelingen / samenloop"
    else:
        advies = "Standaard dienstverlening"

    return advies

def samenvatting(klanten):
    adviezen_telling = {}

    for klant in klanten:
        advies = klant["advies"]
        if advies in adviezen_telling:
            adviezen_telling[advies] += 1
        else:
            adviezen_telling[advies] = 1

    print("Samenvatting:")
    print("Aantal klanten:", len(klanten))
    print("Telling adviezen:")
    for advies, aantal in adviezen_telling.items():
        print(f"- {advies}: {aantal}")


def sla_op_naar_json(klanten, bestandsnaam="klanten.json"):
    with open(bestandsnaam, "w", encoding="utf-8") as bestand:
        json.dump(klanten, bestand, ensure_ascii=False, indent=4)


def main():
    print("KlantAssistent gestart (WerkZeker Nederland)")

    klanten = verwerk_klanten()
    samenvatting(klanten)

    sla_op_naar_json(klanten)
    print("Gegevens opgeslagen in klanten.json")



if __name__ == "__main__":
    main()
