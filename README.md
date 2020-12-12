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
## Luke 1 - ROT24

**Oppgave:**<br />
RUV{JgkJqPåGtFgvLwnKilgp}

**Løsning:**<br />
ROT24 gir løsningen

**Svar:**<br />
PST{HeiHoNåErDetJulIgjen}

---
## Luke 1 - Egg nr 1 🥚 - humans.txt

**Oppgave:**<br />
På nettsiden så finnes det både robots.txt og humans.txt:<br />
https://dass.npst.no/robots.txt<br />
https://dass.npst.no/humans.txt<br />

**Løsning:**<br />
Åpne https://dass.npst.no/humans.txt<br />
Søk etter "egg".

**Svar:**<br />
EGG{sh4rks_d0t_txt}

---

## Luke 2 - Midi fil med hemmelig beskjed

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
## Luke 3 - Cupkake.png bildeforbedring CSI-style

**Oppgave:**<br />
Man får et bilde cupkake.png som skal forbedres.

**Løsning:**<br />
Logg inn på https://npst.no <br />
Velg programmet Forbedre<br />
Last opp bildet og velg Forbedre flere ganger<br />

**Svar:**<br />
PST{HuskMeteren}

---
## uke 3 - Egg nr 2 🥚 - Slede8 bonus

**Oppgave:**<br />
I en zip-fil hadde vi fått en mystisk fil som het kladd.txt. Den startet med åtte emojier av sleder:<br />
🛷🛷🛷🛷🛷🛷🛷🛷 <br />
Fulgt av en lang kode.

**Løsning:**<br />
Åpne http://slede8.npst.no<br />
På toppen av URL skriv inn # fulgt av koden:<br />
https://slede8.npst.no/#N4Igzg9grgTgxgUwMIQCYJALhAZQKIAqBABDAIwA0xADAB5kA6AdgGo4DSAkgGInlXlm+IqWpUAbAE4h7AEqcWo5gAkA8gAV1NWgCYEzZgAsAtsczMAdABEAggRvaALI4p1xAVle0ECLwA4Adi8AI3F-MTpUSjpHXzoAQy9HRMiAMy9JVMtbe214iNp3VC8AnS94sro-AGYMuNpJTzoEJtpUAtQwhJSGnWy7BzoA+tS4ENq6auCQ9Lp3aO9phPqEYqrK+jG6HUcDJnUAGQBVHBxRAUYmDnlFGGoZG6Urwj4xbQDgh4UngiPZYjAAE9UAAHCAAGwQTGYhxOZzuFy+t3u0KuBA06j2QNBEKh5meInILiewj4ZE8pEuzG4nAAcrTiCZjMwABp4A4HPD-GBlUh9Al8Cl0KlMCDGADWADdVvjOfDqswDjYcHxdkw2RyuaRaqQ1YrOOw+QIFUwAEJqTTEMFgAAu4KgqAAllBmVc5N8YCbYadzqR3CoMcQxVLVntrXaHc6zEIXr6iTHCZRKf6mLJCH89swQBQQI6mCCoDasCAyKVJPFgnBqqkpn5JI5quJxMEdAF4qka3B5sEyKh2u1EHBm2RJJJgn50KkAtQ4JIdKgdO5hhUdH4fGQaj4PDsQABfIA<br />
Trykk "Løp" og velg Aa i Oppgulp.

**Svar:**<br />
EGG{SLEDE8ExampleForSPSTInternalUseOnly}

---
## Luke 4 - Database med dager siden påske

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
## Luke 4 - Egg nr 3 🥚 - SQL

**Oppgave:**<br />
?

**Løsning:**<br />
?

**Svar:**<br />
?

---
## Luke 5 - Logg.csv passordbyttefil

**Oppgave:**<br />
Det ble gitt en loggfil (log.csv) hvor brukere hadde endret passordet sitt.


**Løsning:**<br />
Les inn filen i Python <br />
Se etter linjen hvor navn og fult navn ikke stemmer:<br />
*Ni%E2%80%8Bssen!= JuleNissen2020-10-15 08:35:03	Ni%E2%80%8Bssen <Jule Nissen>		SPF <Seksjon for Passord og Forebygging>		I dag har jeg lyst til at PST{879502f267ce7b9913c1d1cf0acaf045} skal være passordet mitt*<br />

**Svar:**<br />
PST{879502f267ce7b9913c1d1cf0acaf045} 


---
## Luke 5 - Egg nr 4 🥚 - Medarbeiderundersøkelse

**Oppgave:**<br />
I innboksen ligger det en e-post fra HR. <br />
*Det er fortsatt mulig å svare på årets medarbeiderundersøkelse:<br />
Skryt meg gjerne opp i skyene, slik at jeg fremstår som en god mellomleder!<br />
Det gjør ved å sende meg en melding til HR med teksten EGG{w0rlds_b3st_b0ss}.*<br />


**Løsning:**<br />
Send svar til HR.

**Svar:**<br />
EGG{w0rlds_b3st_b0ss}

---
## Luke 6 - Slede8

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
## Luke 6 - Egg nr 5 🥚 - Slede8 Hello World

**Oppgave:**<br />
Gå til http://slede8.npst.no og løs e-læring Hello World. <br />


**Løsning:**<br />
Løs e-læring Hello World

**Svar:**<br />
EGG{Hello, SLEDE8!}


---
## Dag 7 - complex16u radiosignal

**Oppgave:**<br />
Syvende luke var et signal som var gitt i filformatet "data.complex16u". Vi skal finne hemmelig beskjed i signalet.


**Løsning:**<br />
complex16u er et radiosignal som kan åpnes med programmet Universal Radio Hacker.<br />
Åpne signalet og velg ASCII. Løsningen kommer opp med en gang.

**Svar:**<br />
PST{0n_0ff_k3y1ng_1s_34sy!}


---
## Luke 8 - ASN1I

**Oppgave:**<br />
Denne dagen fikk man en fil som het "ASN.1 spec". Det er skrevet i språket ANS.1.  Koden vi fikk var:<br />
MIIBOTCCATAwggEnMIIBHjCCARUwggEMMIIBAzCB+zCB8zCB6zCB4zCB2zCB0zCByzCBwzCBuzCBszCBqzCBozCBnDCBlDCBjDCBhDB9MHYwbzBoMGEwWjBTMEwwRTA+MDcwMTAqMCMwHDAVMA4wBwUAoQMCAROgAwIBA6EDAgEMogMCAQChAwIBE6ADAgEBoQMCARKkAgUAoQMCARShAwIBDqIDAgEYoQMCAQShAwIBEqEDAgEOoQMCAQ6hAwIBB6IDAgECogMCAQigAwIBAaIDAgENogMCARKiAwIBAKMCBQCiAwIBE6IDAgESogMCAQ+hAwIBEaEDAgEOoQMCAQugAwIBAKIDAgEDoQMCAQyhAwIBFKEDAgESoQMCAQ+gAwIBAaEDAgEMoAMCAQOhAwIBEaEDAgEOogMCAQs=

**Løsning:**<br />
Åpne https://holtstrom.com/michael/tools/asn1decoder.php og dekod koden.<br />
Hvis man åpner filen "ASN.1 spec" så ser man at hvert enkelt array betyr noe:<br />
[0] digit<br />
[1] lower case alphabet<br />
[2] upper case alphabet<br />
[3] leftCurlyBracket<br />
[3] rightCurlyBracket<br /><br />
Bruk dekodet kode (SEQUENCE) for å finne løsningen, f.eks.:<br />
[1] {INTEGER 0x13 (19 decimal) } er lower case alphabet index 19 som betyr t.")<br />
print("[0] {INTEGER 0x03 (3 decimal) } er lower digit index 3 som betyr 3.")<br /><br />
Les løsningen fra bunn til topp.

**Svar:**<br />
PST{ASN1IChooseYou}



---
## Luke 9 - Hexmax - Hex/16 Emoji replace

**Oppgave:**<br />
Man ble presentert med to linjer emoji. Den første linjen var 16 unike emoji og representerer alfabetet. Den andre er en kodet beskjed.<br />
🎅🤶❄⛄🎄🎁🕯🌟✨🔥🥣🎶🎆👼🦌🛷<br /><br />

🤶🛷✨🎶🎅✨🎅🎅🛷🤶🎄🔥🎆🦌🎁🛷🎅❄🛷🛷🎅🎶🎅✨🎅🦌🥣🔥🛷🦌⛄🎅🌟🛷🛷🔥🎄🦌🎅✨🦌🦌🕯🎶🎅🤶🦌❄🎁🕯🎅✨🎶👼🌟🎆🕯🌟❄👼🎅🎅🤶❄🎄👼🎆🔥🎁🛷🤶👼🎅🎅🎅🎅🎅🎅



**Løsning:**<br />
Les inn den første linjen som hex, fra 0-F. Du skal da ha Nisse=0, Nissemor=1, Snøkrystall=2, ..., Slede=F<br />
Bruk mappingen og konverter alle emoji i beskjeden om til hex, du skal da sitte igjen med koden:<br />
*1F8B0800F149CE5F02FF0B080EA9FE307FF94E08EE6B01E25608BD7C672D00124DC95F1D000000*<br />
Starten på hex filen, 1F8B08, sier at dette er en zip-fil. <br />
Åpne HxD eller annen hex editor, lim inn koden og lagre som solution.gz. Åpne solution.gz i WinRar. Du skal da få løsningen.

**Svar:**<br />
PST{🧹🧹🎄🎅🎄🧹}


---
## Luke 10 - Slede8 (A + B) mod 256 som en ASCII-streng

**Oppgave:**<br />
På https://slede8.npst.no/ så skulle vi legge inn e-læringskode 82ec70284b51eb12 som ga følgende oppgave:<br />
Slede8 (A + B) mod 256.<br />
Slede 8 har ikke modolu, gange eller dele. Men det har pluss, minus og mindre enn.


**Løsning:**<br />
......

**Svar:**<br />
PST{++AndKissesWillBeAwardedToYou}


---
## Luke 10 - Egg nr 7 🥚 - Slede8: A+B

**Oppgave:**<br />
Gå til http://slede8.npst.no og løs E-læring 8e7c9876c85e5471. <br />


**Løsning:**<br />
Se Day_10_easter_slede8.txt<br />
Send egget til HR i mail.

**Svar:**<br />
EGG{ba92ae3a9af1a157703ca83d9a9fb11d}


---
## Luke 11 - SQLite database med md5 sum av fornavn og etternavn

**Oppgave:**<br />
Vi fikk en databasefil liste.db samt to andre småfiler. Databasefilen kan åpnes i DB Browser for SQLite. <br />
Tabellene hadde fornavn, etternavn og md5-sum. En av md5-summene var feil, vi skulle finne hvilken. 



**Løsning:**<br />
Kjør checkpoint først på databasen, for å få den til å bli synkronisert. Dette gjøres ved å kjøre følgende spørringer:<br />
*PRAGMA wal_autocheckpoint = 0<br />
PRAGMA wal_checkpoint(PASSIVE)*<br /><br />

Skriv deretter ut alle radene i begge tabellene og kjør md5 på fornavn etternavn. Skriv ut den linjen som ikke matchet. 


**Svar:**<br />
PST{49422712408d5409a3e40945204314e6}

---
## Luke 12 - Slede8 Reverse engineering

**Oppgave:**<br />
I dag fikk vi et program "program.s8" som er eksportert ut fra slede8.npst.no <br />
https://github.com/PSTNorge/slede8/



**Løsning:**<br />
FUNKER IKKE...<br />
Last ned Nodejs og installer https://nodejs.org/en/<br />
Last ned Visual Studio Community og installer https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=Community&rel=16<br />
Åpne "x64 Native Tools Command Prompt for VS 2019" og skriv: *npm install -g typescript*<br />
*npm install rollup --save-dev*<br />
Åpne Visual Studio Installer og installer Visual Studio Community (uten workload)<br />
Checkout prosjektet fra https://github.com/PSTNorge/slede8 i Visual Studio<br /><br />

Åpne cmd og skriv kommandoene:<br />
cd C:\Users\user\source\repos\slede8<br />
npm install<br />
npm run build<br /><br />

Åpne Slede8 program:<br />
https://slede8.npst.no#N4Igzg9grgTgxgUwMIQCYJALhAHQHb4DKAogCqkAEMAjAAwA0FtRZlN1j1++AcgPIAFYr0HC8-IRQDcFAA4BTingRgALggoAbAJZ4AVhoQwK6VRQRnZUPAGszq7ZvOr1MVQENbCAITdxoihEhP1IAVQAlCjAbGG0ANwB9AAtHMAQ8aQobd01NIwoAcgAzaxswPQhlPAKomPjk1PT8MMj01BgEBKKAD5g1ToAjCDKPRIdNBLAAW3kEuKMwHKNmiNrYxJTNNII8QlJBAT90hJ11PAat9Mx8ADoAEQBBUgeKAA4OAE4AdnoOag+ACy-ABsf0Bvy+PzBAFZfgAmD6-cHUADMHBRSKB1ABsLhwPo+Lh9CBGOo2PosNesLoGJRUPJdIpDDhHABQNeRPxH1e9ChtDBWKp9CF-yxX0JpORwMR-2p0t5mIhRIB6MV1C+iNx+PxKNhWoJwo472FULxvzov1oDDJMp5r01+NlEJlyJRPK+nJhEKNpLhsJRkrFuJ5ooh7IYjKFwIxX2pZPNWPJdD+tHpOpj1v5luptB5AeJ9CJUKlRKd1GhGMJRKJIuR4sLQMdHAYLforfbbc77b8+Gi6wu22ueAAYgBJHg8cznU7HTbbTJ9+IUdyodoqefjLTuAYIPIZArHGfnOfpGqbmC0CgQADmVC4O0XiWU-TmRlQ2iHABkHnsqHCKABgGZJo7hqBQ8wwO+6RRBAUwUAMOjGLICB2HIii6Bk2h-vgn6jgA0n+jA0JeAEyEkcTaGA4Fvto0H5DoNhMMucRgJoUAuPkFH4AAQgAEgcaz1Ce5wlLkPRuEQeHhKOABq2F4AIn6hIQhBUAwd7UMBCDXremnnuprHaIx7hmBRSiKMhNj5AoSgqOo1GQVhWGoCZ7hNBkQGeUBMh8NxhDeBQ5GUeBWHXnovQmBY9k3mpFDXvIxhFDA7hMAAHsOw4ALQAHy0KlVoUDMIVyGxYBpGhFD3l51WZFhHTXpRrgWHeAEABR5RlFAANRpfyFAALxpXQtAAJQ3BQdzNUk8h4KgTVUUZVmBcseD8QIAiCU+dmdBB75+I+A7HKJmjiaoQ7hGQEQ9jsbQdF0vQvkMIzuGMjiTDMr59EsMBDmOE5Tic2hnIdOzfr+MD-jVMgQwNFAehQrUFLxBQjSw5BUBiaVwiRmT4IpymqRDREot5f6wwUSQFDhDwAOKRDDUObQ5UGYWT4wDO4S2biuHRldBkBwReV63jQcgodZ8j4BdLTXSA9AgLoViqFgIAgAAvkAA

<br /><br />
I nettleseren velg Consoll på siden. Legg så denne koden inn:<br />
localStorage.setItem('🚲', 10000) <br />

**Svar:**<br />


