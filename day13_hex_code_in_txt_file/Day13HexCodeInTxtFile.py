# Filename: Day13HexCodeInTxtFile.py
# Author: S Ditlefsen
# Date 13 Dec 2020
# License: http://opensource.org/licenses/gpl-license.php GNU Public License


# About class:
#

# Assignment:
#   Følgende melding ble tilsendt NPST per faks, og ingen i postmottaket forstår innholdet. Det ser ut som den bruker en eller annen form for hex-enkoding, men selv hex-dekodet gir faksen ingen mening.
#
#   Klarer du å finne mening i meldingen?



class Day13HexCodeInTxtFile:
    print('')
    print('~~~~~~~~~~~~~~~~~~~~~~~~ Day 13 ~~~~~~~~~~~~~~~~~~~~~~~~')
    print('~~~~~~~~~~~~~~~~ Hex code from Fax machine ~~~~~~~~~~~~~')
    print('')

    """ Read Hex file ---------------------------------------------------------------- """
    def readHexFile(fileName):
        # Read file
        print("Read file " + fileName)
        read = repr(open(fileName, 'r').read())
        print(read)
        return read


    """ Script start ---------------------------------------------------------------- """
    read_file = readHexFile("./day13_hex_code_in_txt_file/melding.txt")
