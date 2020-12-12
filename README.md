# npst_2020 :: PST Julekalender 2020 
## Capture The Flag

**About**

This project contains soultions for xmas calendar at https://npst.no.
The solution is programmed in Python.

**How to install**
1. Download and install Git from https://git-scm.com/downloads
2. Download and install Python 3.9 or newer from https://www.python.org/downloads/
3. Download and install PyCharm from https://www.jetbrains.com/pycharm/download/
4. In PyCharm create new project from Git with URL https://github.com/europa9/npst_2020.git

**How to run**

Go to main.py and click Shift+F10 to run code.

---
## Dag 1

**Oppgave:**<br />
RUV{JgkJqPåGtFgvLwnKilgp}

**Løsning:**<br />
ROT24 gir løsningen

**Svar:**<br />
PST{HeiHoNåErDetJulIgjen}

---
## Dag 2

**Oppgave:**<br />
Etteretningsoffiseren GWYN, Pen ble stoppet i tollen ved utreise den 25. november. Vi sikret i den forbindelse et lagringsmidie som inneholdt en mystisk fil. Kan du analysere filen pen_gwyn_greatest_hits.mid?<br />
Det er fortsatt uvisst hvorfor GWYN befant seg på Nordpolen på dette tidspunktet, men han skal ha blitt observert på det lokale vannhullet Svalbar.

**Løsning:**<br />
Åpne filen som hex "pen_gwyn_greatest_hits.mid".<br />
Les fra byte 194<br />
Les hver 22. hex verdi<br />

**Svar:**<br />
ABCDEFGHIJKLMNOPQRSPST{BabyPenGwynDuhDuhDuhDuhDuhDuh}TSRQPONMLKJIHGFEDCBA@?>=\


---
## Dag 3

**Oppgave:**<br />
Man får et bilde cupkake.png som skal forbedres.

**Løsning:**<br />
Logg inn på https://npst.no <br />
Velg programmet Forbedre<br />
Last opp bildet og velg Forbedre flere ganger<br />

**Svar:**<br />
PST{HuskMeteren}

---
## Dag 4

**Oppgave:**<br />
Det ble gitt en databasefil som skulle regne ut 
påskedag og antall dager mellom 1. jan 1900 og
påskedag i det gitte året fra 2020-2040.<br />
Til slutt skulle man summere antall tallet (antall dager).

**Løsning:**<br />
2020-04-12	43930<br />
2021-04-04	44287<br />
2022-04-17	44665<br />
...<br />
2039-04-10	50867<br />
2040-04-01	51224<br />

**Svar:**<br />
PST{999159}



---
## Dag 5

**Oppgave:**<br />
Det ble gitt en loggfil (log.csv) hvor brukere hadde endret passordet sitt.


**Løsning:**<br />
Les inn filen i Python <br />
Se etter linjen hvor navn og fult navn ikke stemmer:<br />
*Ni%E2%80%8Bssen!= JuleNissen2020-10-15 08:35:03	Ni%E2%80%8Bssen <Jule Nissen>		SPF <Seksjon for Passord og Forebygging>		I dag har jeg lyst til at PST{879502f267ce7b9913c1d1cf0acaf045} skal være passordet mitt*<br />

**Svar:**<br />
PST{879502f267ce7b9913c1d1cf0acaf045} 



---
## Dag 6

**Oppgave:**<br />
PST har laget et program som heter slede8. Det kan ses her: http://slede8.npst.no.
Inne på programmet skal man ta "E-læring" Hei Verden, Enkel addisjon og Manuell 4032996b1bbb67f6.


**Løsning:**<br />
Løs Hei Verden <br />
Løs Enkel addisjon<br />
Løs Manuell 4032996b1bbb67f6<br />

**Svar:**<br />
PST{ATastyByteOfSled}

---
## Dag 7

**Oppgave:**<br />
Syvende luke var et signal som var gitt i filformatet "data.complex16u". Vi skal finne hemmelig beskjed i signalet.


**Løsning:**<br />
complex16u er et radiosignal som kan åpnes med programmet Universal Radio Hacker.<br />
Åpne signalet og velg ASCII. Løsningen kommer opp med en gang.

**Svar:**<br />
PST{0n_0ff_k3y1ng_1s_34sy!}

