# Filename: Day13HexCodeInTxtFile2Solve.py
# Author: S Ditlefsen
# Date 13 Dec 2020
# License: http://opensource.org/licenses/gpl-license.php GNU Public License


# About class:
#

# Assignment:
#   Følgende melding ble tilsendt NPST per faks, og ingen i postmottaket forstår innholdet.
#   Det ser ut som den bruker en eller annen form for hex-enkoding, men selv hex-dekodet gir faksen ingen mening.
#
#   Klarer du å finne mening i meldingen?
from collections import Counter


class Day13HexCodeInTxtFile2Solve:
    print('')
    print('~~~~~~~~~~~~~~~~~~~~~~~~ Day 13 ~~~~~~~~~~~~~~~~~~~~~~~~')
    print('~~~~~~~~~~~~~~~~ Hex code from Fax machine ~~~~~~~~~~~~~')
    print('~~~~~~~~~~~~~~~~~~~~~~~~ (2) Solve ~~~~~~~~~~~~~~~~~~~~~')
    print('')

    # Replacement pattern from last
    replacement_chars_a = {"7", "F", "5", "1", "E", "C", "2", "3"}
    replacement_chars_b = {"4", "6", "A", "9", "B", "0", "8", "D"}
    replacement_character_a = " "
    replacement_character_b = "X"

    # Read file
    file = open("./day13_hex_code_in_txt_file/melding.txt", "r")
    for line in file:
        for letter in replacement_chars_a:
            line = line.replace(letter, replacement_character_a)

        for letter in replacement_chars_b:
            line = line.replace(letter, replacement_character_b)

        print(line, end="")

    # Solution
    # PST{SNEAKY_FLAG_IS_SNEAKY}