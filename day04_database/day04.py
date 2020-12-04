# Filename: day04.py
# Author: S Ditlefsen
# License: http://opensource.org/licenses/gpl-license.php GNU Public License


# About class:
#   Creates a SQLite database
#   Runs commands

# Assignment:
#   Vi i mellomledergruppa er svært interessert i måltall, og ledelsen ønsker en rapport snarest på summen av kolonnen Maaltall fra og med 2020 til og med 2040. Kan du svare meg med denne summen, omkranset av PST{ og } når du finner ut av det?

import datetime


class Day04:
    print('')
    print('~~~~~~~~~~~~~~~~~~~~~~~~ Day 04 ~~~~~~~~~~~~~~~~~~~~~~~~')

    def dateEaster(year):
        if year >= 1900 and year <= 2099:
            a = year % 19
            b = year % 4
            c = year % 7
            d = (19 * a + 24) % 30
            e = (2 * b + 4 * c + 6 * d + 5) % 7
            dateofeaster = 22 + d + e
            if year == 1954 or year == 1981 or year == 2049 or year == 2076:
                dateofeaster = dateofeaster - 7

            if dateofeaster > 31:
                dateofeaster = dateofeaster - 31

                if(dateofeaster < 10):
                    dateofeaster = "0" + str(dateofeaster);


                print(str(year) + "-04-" + str(dateofeaster)+ "\t", end='')
            else:
                print(str(year) + "-03-" + str(dateofeaster)+ "\t", end='')
        else:
            print("There is an error")

    """ Scriptstart """

    # Print header
    print("DatoPaaskeId\tPaaskeAften\tPaaskeFerieUke\tAar\tMaalTall")
    print("------------ ---------------- -------------- ------ -----------")
    x=0
    for year in range(2020, 2039):
        x=x+1

        ## Print ID
        print(str(x) + "\t", end='')

        # Print easter day
        dateEaster(year)

        # New line
        print(" ")