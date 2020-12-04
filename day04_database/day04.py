# Filename: day04.py
# Author: S Ditlefsen
# License: http://opensource.org/licenses/gpl-license.php GNU Public License


# About class:
#   Creates a SQLite database
#   Runs commands

# Assignment:
#   Vi i mellomledergruppa er svært interessert i måltall, og ledelsen ønsker en rapport snarest på summen av kolonnen Maaltall fra og med 2020 til og med 2040. Kan du svare meg med denne summen, omkranset av PST{ og } når du finner ut av det?

import datetime
from datetime import datetime
from datetime import date

class Day04:
    print('')
    print('~~~~~~~~~~~~~~~~~~~~~~~~ Day 04 ~~~~~~~~~~~~~~~~~~~~~~~~')

    """- MeasurementNumber = Days between input date and 1900 -----------------"""
    def measurementNumber(paaskeaften):
        d0 = date(1900, 1, 1)
        paaskeaften = paaskeaften.split("-")
        year = paaskeaften[0]
        month = paaskeaften[1]
        day = paaskeaften[2]
        d1 = date(int(year), int(month), int(day))
        delta = d1 - d0

        # print measurement number
        print(str(delta.days-1) + "\t", end='')

        return(delta.days-1)

    """- DateEaster = Date when easter day is ---------------------------------"""
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
                easterDay = str(year) + "-04-" + str(dateofeaster)
            else:
                print(str(year) + "-03-" + str(dateofeaster)+ "\t", end='')
                easterDay = str(year) + "-03-" + str(dateofeaster)
        else:
            print("There is an error")
        return easterDay

    """- Scriptstart ----------------------------------------------------------"""
    # Print header
    print("DatoPaaskeId\tPaaskeAften\tPaaskeFerieUke\tAar\tMaalTall")
    print("------------ ---------------- -------------- ------ -----------")
    x=0
    sum = 0
    for year in range(2020, 2041):
        x=x+1

        ## Print ID
        print(str(x) + "\t", end='')

        # Print easter day + measurement number
        measurement_number = measurementNumber(dateEaster(year))

        # Sum measurement numbers (solution is sum of measurement numbers)
        sum += measurement_number

        # New line
        print(" ")

    # Print solution
    print("PST{"+str(sum)+"}")
