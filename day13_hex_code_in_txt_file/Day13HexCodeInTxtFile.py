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
        file = open(fileName, "r")

        # Repeat for each song in the text file
        x = 0
        line_len = 0
        number_of_bytes_per_line = 0
        total_number_of_bytes = 0
        for line in file:
            line = line.replace('\n', '')
            line_len = len(line)
            number_of_bytes_per_line = line_len/2
            total_number_of_bytes = total_number_of_bytes + number_of_bytes_per_line;
            print("Line " + str(x) + ", len " + str(line_len) + ", bytes " + str(number_of_bytes_per_line) + ": " + str(line))

            x = x + 1;

        # Print summary of data
        print("\n")
        print("Lines of data: " + str(x))
        print("Character per line: " + str(line_len))
        print("Bytes per line: " + str(number_of_bytes_per_line))
        print("Total number of bytes: " + str(total_number_of_bytes))

        return file


    """ Script start ---------------------------------------------------------------- """
    read_file = readHexFile("./day13_hex_code_in_txt_file/melding.txt")
