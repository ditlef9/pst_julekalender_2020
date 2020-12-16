# Filename: Day13HexCodeInTxtFile1FindPattern.py
# Author 1: S Ditlefsen
# Author 2: Julebokk
# Date 14 Dec 2020
# License: http://opensource.org/licenses/gpl-license.php GNU Public License


# About class:
#

# Assignment:
#   Det nyeste innen måltallsrapportering er antall fullførte e-læringsmoduler i SLEDE8 blandt de ansatte,
#   så kunne du gjennomført modul 97672649875ca349? Rapporter tilbake som vanlig når du er ferdig!
#
#   Utviklerverktøyet finner du fortsatt her. Se vedlagt dokumentasjon, eller på GitHub.


class Day14Slede8LittleEndian:
    print('')
    print('~~~~~~~~~~~~~~~~~~~~~~~~ Day 14 ~~~~~~~~~~~~~~~~~~~~~~~~')
    print('~~~~~~~~~~~~~~~~~~ Slede 8 Little Endian ~~~~~~~~~~~~~~~')
    print('')


    inp = [0x11, 0x22, 0xff, 0xdd, 0xaa, 0x33, 0x55, 0x00]
    rev = []
    i = 0

    while inp[i] != 0x00:
        rev = [inp[i]] + rev
        i += 1
    print([hex(i) for i in rev])