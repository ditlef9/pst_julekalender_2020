# Filename: Day09Hexmax.py
# Author: S Ditlefsen
# License: http://opensource.org/licenses/gpl-license.php GNU Public License

# Assignment:
#   En samarbeidende tjeneste har sendt oss en chatlogg fra en antatt SPST agent. Meldingen vekket oppsikt pga den overdrevne bruken av emojier. Meldingen ser ut til å være obfuskert på en eller annen måte som ikke er kjent for oss fra tidligere beslag.
#
#   Vi lurer på om det kan være brukt HEXMAS-enkoding. Kan du undersøke det nærmere?
#
#     🎅🤶❄⛄🎄🎁🕯🌟✨🔥🥣🎶🎆👼🦌🛷
#
#     🤶🛷✨🎶🎅✨🎅🎅🛷🤶🎄🔥🎆🦌🎁🛷🎅❄🛷🛷🎅🎶🎅✨🎅🦌🥣🔥🛷🦌⛄🎅🌟🛷🛷🔥🎄🦌🎅✨🦌🦌🕯🎶🎅🤶🦌❄🎁🕯🎅✨🎶👼🌟🎆🕯🌟❄👼🎅🎅🤶❄🎄👼🎆🔥🎁🛷🤶👼🎅🎅🎅🎅🎅🎅
from collections import Counter


class Day09Hexmax:
    print('')
    print('~~~~~~~~~~~~~~~~~~~~~~~~ Day 09 ~~~~~~~~~~~~~~~~~~~~~~~~')

    # Input
    hexmax_a = "🎅🤶❄⛄🎄🎁🕯🌟✨🔥🥣🎶🎆👼🦌🛷"
    hexmax_b = "🤶🛷✨🎶🎅✨🎅🎅🛷🤶🎄🔥🎆🦌🎁🛷🎅❄🛷🛷🎅🎶🎅✨🎅🦌🥣🔥🛷🦌⛄🎅🌟🛷🛷🔥🎄🦌🎅✨🦌🦌🕯🎶🎅🤶🦌❄🎁🕯🎅✨🎶👼🌟🎆🕯🌟❄👼🎅🎅🤶❄🎄👼🎆🔥🎁🛷🤶👼🎅🎅🎅🎅🎅🎅"
    alphabet_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


    # Hexmax A
    print("\nHexmax A")
    print("Length: " + str(len(hexmax_a)))
    print("Emoji\tUnicode\tOccurence\tLetter")
    counter = Counter(hexmax_a)
    x = 0
    for emoji in hexmax_a:
        unicode = f'U+{ord(emoji):X}'
        occurence = counter[emoji]
        letter = alphabet_uppercase[x]
        print(emoji + "\t" + unicode + "\t" + str(occurence) + "\t" + letter)

        x = x+1

    # Hexmax B
    print("\nHexmax B")
    print("Length: " + str(len(hexmax_b)))
    print("Emoji\tUnicode\tOccurence")
    counter = Counter(hexmax_b)
    x = 0
    for emoji in hexmax_b:
        unicode = f'U+{ord(emoji):X}'
        occurence = counter[emoji]

        print(emoji + "\t" + unicode + "\t" + str(occurence))

        x=x+1

