# Filename: day07_signal.py
# Author: S Ditlefsen
# License: http://opensource.org/licenses/gpl-license.php GNU Public License

# Assignment:
#   Det har blitt fanget opp et rart signal her på julenissens verksted.
#   Det ser ikke ut til at det er et kontinuerlig signal, da det ser til å komme og gå litt.
#   Klarer du å finne ut hva det er?

class Day07Signal:
    print('')
    print('~~~~~~~~~~~~~~~~~~~~~~~~ Day 07 ~~~~~~~~~~~~~~~~~~~~~~~~')

    # Read file and loop trough it
    read_file = repr(open("./day07_signal/data.complex16u", 'rb').read())
    string_solution=""

    for char in read_file:
        print(char, end='')