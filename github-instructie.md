# Trainee instructie: van clone tot eerste push

Gebruik deze handleiding om de opdracht van de trainer op te halen en daarna in je **eigen GitHub-repository** te zetten.


## Wat heb je nodig?

- Git is geïnstalleerd
- Je hebt een GitHub-account
- Je hebt de URL van de repository van de trainer

---

## Stap 1: Clone de repository van de trainer

Klik op Open folder binnen vscode en ga naar de map python-projects op je c schijf

Open je terminal en voer dit commando uit:

```bash
git clone <url-van-de-repo-van-de-trainer>

git clone https://github.com/jelmer-calco/python-client-assistent

Stap 2: Ga naar de map van het project
cd python-fundamentals-exercises

Stap 3: Maak op GitHub een nieuwe lege repository aan

Ga naar GitHub en maak in je eigen account een nieuwe repository aan.

Kies een duidelijke naam, bijvoorbeeld:

python-opdracht-jouwnaam
python-vervolgopdrachten-jouwnaam

Maak deze repository leeg aan.

Dus: verder niks aanklikken qua gitignore ed


voeg geen license toe
Stap 4: Verwijder de koppeling met de repository van de trainer

git remote remove origin



Stap 5: Koppel je lokale project aan je eigen repository
Voeg nu jouw eigen GitHub-repository toe als nieuwe origin:
kies hieronder de url voor jouw repop
git remote add origin https://github.com/jelmer-calco/test.git
git branch -M main
git push -u origin main

Voorbeeld:
git remote add origin https://github.com/jouw-gebruikersnaam/python-opdracht-jouwnaam.git

Stap 6: Controleer of de koppeling goed staat
Controleer met welk adres je project nu verbonden is:
git remote -v
Je moet nu de URL van jouw eigen GitHub-repository zien.


Stap 7: Doe je eerste push

Push nu het project naar jouw eigen GitHub-repository:

git push -u origin main

Na deze stap staat het project in jouw eigen repository op GitHub.

Stap 8: switch van branch

git checkout -b branch-name

Stap 9: Sla wijzigingen op en push opnieuw

Pas iets aan in een van de files. Sla de file op (ctrl s)
Als je iets hebt aangepast, gebruik je steeds deze commando’s:

git add .
git commit -m "Beschrijving van je wijziging"
git push

Voorbeeld:

git add .
git commit -m "Opdracht 1 gemaakt"
git push
Overzicht van de belangrijkste commando’s
git clone <url-van-de-repo-van-de-trainer>
cd python-vervolgopdrachten
git remote remove origin
git remote add origin <url-van-jouw-eigen-repository>
git branch -M main
git push -u origin main

Daarna werk je verder met:

git add .
git commit -m "Beschrijving van je wijziging"
git push

