"""
CODE KICKSTART — KlantAssistent (WerkZeker Nederland)
-----------------------------------------------------

Context:
Dit project is onderdeel van de training Code Kickstart.
Je bouwt een eenvoudige Python applicatie die gegevens van burgers/aanvragers verwerkt
en op basis daarvan één advieslabel genereert.

De tool is beslisondersteunend: het advies is een intern signaal voor de medewerker.
De tool voert geen acties uit, kent geen rechten toe en neemt geen echte besluiten.

Doel:
- Oefenen met Python fundamentals (variables, types, if/elif/else, loops)
- Denken in iteraties
- Vertalen van pseudocode naar Python
- Structureren met dicts/lists en functies (parameters + return)

Spelregels:
- Werk stap voor stap
- Test elke iteratie
- Houd de code leesbaar
- Werk toe naar een werkende terminal-applicatie
"""

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
    """
    Vraagt gegevens van één klant/aanvrager en retourneert een dictionary.

    Verwachte keys in de dictionary:
    - naam (str)
    - leeftijd (int)
    - besteding (float)  -> bestedingsniveau per maand in euro's
    - klanttype (str)    -> 'nieuw', 'bestaand', 'premium'

    Denkstappen (pseudocode):
    1. Vraag de naam
    2. Vraag de leeftijd (moet int worden)
    3. Vraag het bestedingsniveau (moet float worden)
    4. Vraag het klanttype (alleen nieuw/bestaand/premium)
    5. Stop alles in een dictionary
    6. Return de dictionary

    Let op (iteratie 4):
    - Leeftijd en besteding moeten getallen zijn (anders opnieuw vragen)
    - Klanttype mag alleen geldige waarden hebben (anders opnieuw vragen)
    """

    klant = {
        "naam": None,
        "leeftijd": None,
        "besteding": None,
        "klanttype": None,
        "advies": None
    }

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

    klant.update({
        "naam": naam,
        "leeftijd": leeftijd,
        "besteding": besteding,
        "klanttype": klanttype
    })

    return klant



def genereer_advies(klant):
    """
    Ontvangt één klant (dictionary) en retourneert één advieslabel (string).

    Advieslabels (exact deze strings gebruiken):
    - 'AOW-check en extra begeleiding'
    - 'Check aanvullende regelingen / samenloop'
    - 'Intensievere begeleiding (complex dossier)'
    - 'Standaard dienstverlening'

    Regels + prioriteit (hoog -> laag):
    1) Klanttype == 'premium' -> 'Intensievere begeleiding (complex dossier)'
    2) Leeftijd >= 67         -> 'AOW-check en extra begeleiding'
    3) Besteding > 100        -> 'Check aanvullende regelingen / samenloop'
    4) Anders                 -> 'Standaard dienstverlening'

    Denkstappen:
    1. Lees waarden uit de dictionary
    2. Gebruik if / elif / else in de juiste volgorde (prioriteit)
    3. Return één advieslabel
    """
    
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
    """
    Print een samenvatting van alle klanten en adviezen.

    Verwachting (minimaal):
    - Print het aantal klanten
    - Print per advieslabel hoe vaak deze voorkomt

    Denkstappen:
    1. Loop over de lijst met klanten
    2. Bepaal per klant het advies (gebruik genereer_advies)
    3. Tel de adviezen (bijv. met een dict)
    4. Print het overzicht netjes
    """

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
    """
    Hoofdprogramma van de applicatie.

    Programmaflow (pseudocode):
    1. Print startbericht
    2. Vraag hoeveel klanten worden ingevoerd (moet int zijn)
    3. Maak een lege lijst voor klanten
    4. Gebruik een loop om klanten te verzamelen (verzamel_klant)
    5. Print per klant het advieslabel (genereer_advies)
    6. Toon een samenvatting (samenvatting)
    """
    print("KlantAssistent gestart (WerkZeker Nederland)")

    klanten = verwerk_klanten()
    samenvatting(klanten)

    sla_op_naar_json(klanten)
    print("Gegevens opgeslagen in klanten.json")



if __name__ == "__main__":
    main()
