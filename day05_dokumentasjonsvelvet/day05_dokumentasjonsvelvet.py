# Filename: day05_dokumentasjonsvelvet.py
# Author: S Ditlefsen
# Date 5 Dec 2020
# License: http://opensource.org/licenses/gpl-license.php GNU Public License


# About class:
#   To get todays assignment you need to adjust the clock in the system.
#   Click on the clock on the bottom right on DASS

# Assignment:
#   Det rapporteres om tilgangstrøbbel til dokumentasjonsvelvet.
#   Vi har fått logger fra Seksjon for passord og forebygging i perioden der man mistenker at feilen kan ligge.
#   Finner dere noe 🧁 i loggene?



class Day05Dokumentasjonsvelvet:
    print('')
    print('~~~~~~~~~~~~~~~~~~~~~~~~ Day 05 ~~~~~~~~~~~~~~~~~~~~~~~~')
    print('~~~~~~~~~~~~~~~~~ Documentation Velvet ~~~~~~~~~~~~~~~~~')
    print('')
    print('To get todays assignment you need to adjust the clock in the system.')
    print('Click on the clock on the bottom right on DASS')
    print('')

    def processLogFile():
        # Header
        print("Datetime\t", end='')
        print("Name\t", end='')
        print("Section\t", end='')
        print("Message")

        # Temp variables
        date_last = "2020-10-01 07:00:04"

        # Read and loop line by line

        with open('./day05_dokumentasjonsvelvet/log.csv', 'r', encoding='utf-16-le') as file1:
            for line in file1:

                line = line.strip()
                line = line.replace('+', ' ')
                line = line.replace('%C3%A6', 'æ')
                line = line.replace('%C3%B8', 'ø')
                line = line.replace('%C3%A5', 'å')
                line = line.replace('%C3%85', 'Å')
                line = line.replace('%C3%98', 'Ø')
                line = line.replace('%7B', '{')
                line = line.replace('%7D', '}')
                line = line.replace('%3C', '<')
                line = line.replace('%3E', '>')
                date = ""
                name = ""
                section = ""
                message = ""

                for i, d in enumerate(line.split(";")):
                    if(i == 0):
                        date = d
                    elif(i == 1):
                        name = d
                    elif(i == 2):
                        section = d
                    elif(i == 3):
                        message = d

                # Body
                if(name != ""):


                    # Check that date is valid
                    if(date < date_last):
                        print(str(date) + "\t", end='')
                        print(str(name) + "\t\t", end='')
                        print(str(section) + "\t\t", end='')
                        print(str(message))

                    # Name check
                    names = name.split('<')
                    names[0] = names[0].replace(' ', '')
                    names[1] = names[1].replace('>', '')
                    names[1] = names[1].replace(' ', '')

                    if(names[0] != names[1]):
                        print(names[0] + "!= " + names[1], end='')
                        print(str(date) + "\t", end='')
                        print(str(name) + "\t\t", end='')
                        print(str(section) + "\t\t", end='')
                        print(str(message))

                    # Variable transfer
                    date_last = date;

    """ Script start """
    processLogFile()
