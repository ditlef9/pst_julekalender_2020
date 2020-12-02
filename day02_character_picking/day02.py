# Filename: day02_character_picking.py
# Author: K Overskeid
# License: http://opensource.org/licenses/gpl-license.php GNU Public License

# Assignment:
#   Etteretningsoffiseren GWYN, Pen ble stoppet i tollen ved utreise den 25. november. Vi sikret i den forbindelse et lagringsmidie som inneholdt en mystisk fil. Kan du analysere filen pen_gwyn_greatest_hits.mid?
#
#   Det er fortsatt uvisst hvorfor GWYN befant seg på Nordpolen på dette tidspunktet, men han skal ha blitt observert på det lokale vannhullet Svalbar.

class Day02:
    print('')
    print('~~~~~~~~~~~~~~~~~~~~~~~~ Day 02 ~~~~~~~~~~~~~~~~~~~~~~~~')
    string = repr(open("./day02_character_picking/pen_gwyn_greatest_hits.mid", 'rb').read())
    string_solution=""
    start_position = 194
    interval = 22
    i = 0
    char_number = 0

    for char in string:
        char_number+=1
        i+=1
        if char_number > start_position:
            if i>=interval:
                string_solution=string_solution+char
                i=0
    print(string[start_position:])
    print(string_solution)