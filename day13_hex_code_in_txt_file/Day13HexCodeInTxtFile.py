# Filename: Day13HexCodeInTxtFile.py
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


class Day13HexCodeInTxtFile:
    print('')
    print('~~~~~~~~~~~~~~~~~~~~~~~~ Day 13 ~~~~~~~~~~~~~~~~~~~~~~~~')
    print('~~~~~~~~~~~~~~~~ Hex code from Fax machine ~~~~~~~~~~~~~')
    print('')

    """ Read Hex file ---------------------------------------------------------------- """
    def readHexFile(fileName):
        # Read file
        print("--- Read file " + fileName + " ---")
        file = open(fileName, "r")
        return_string = "";


        # Dictionary
        #frequency_analysis = dict()

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

            # Go trough each byte
            #y = 0
            #for character in line:
            #    print("Line " + str(x) + " Char " + str(y) + ": " + character)
            #    y = y + 1

            # Return string
            return_string = return_string + line;

            x = x + 1;

        # Print summary of data
        print("\n")
        print("Lines of data: " + str(x))
        print("Character per line: " + str(line_len))
        print("Bytes per line: " + str(number_of_bytes_per_line))
        print("Total number of bytes: " + str(total_number_of_bytes))

        return return_string

    """ Count chacaters -------------------------------------------------------------- """
    def count_chars(check_string):
        print("\n--- Count characters ---")
        print("Counting characters in " + check_string)
        dictionary = dict()

        for s in check_string:
            if s in dictionary:
                dictionary[s] += 1
            else:
                dictionary[s] = 1

        # Print dictionary
        print("\nDictionary first to last:")
        for key in dictionary:
            print(key, dictionary[key])

        # Print first to last
        convert_string = ""
        counter = Counter(check_string)
        print('\nDictionary sorted on most common:')
        for letter, count in counter.most_common(500):
            print(str(letter) + " " + str(count))

            convert_string = convert_string + " 0x" + str(count)

        # Convert string
        print("\nString to convert:")
        print(convert_string)


    """ Script start ---------------------------------------------------------------- """
    read_file = readHexFile("./day13_hex_code_in_txt_file/melding.txt")
    count_chars(read_file)