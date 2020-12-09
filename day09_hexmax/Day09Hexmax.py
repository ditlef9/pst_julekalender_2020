# Filename: Day09Hexmax.py
# Author: S Ditlefsen
# License: http://opensource.org/licenses/gpl-license.php GNU Public License

# Assignment:
#   En samarbeidende tjeneste har sendt oss en chatlogg fra en antatt SPST agent.
#   Meldingen vekket oppsikt pga den overdrevne bruken av emojier.
#   Meldingen ser ut til å være obfuskert på en eller annen måte som ikke er kjent
#   for oss fra tidligere beslag.
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


    def printOverview():

        # Code to break
        secret_code = "🤶🛷✨🎶🎅✨🎅🎅🛷🤶🎄🔥🎆🦌🎁🛷🎅❄🛷🛷🎅🎶🎅✨🎅🦌🥣🔥🛷🦌⛄🎅🌟🛷🛷🔥🎄🦌🎅✨🦌🦌🕯🎶🎅🤶🦌❄🎁🕯🎅✨🎶👼🌟🎆🕯🌟❄👼🎅🎅🤶❄🎄👼🎆🔥🎁🛷🤶👼🎅🎅🎅🎅🎅🎅"

        # Input
        alphabet_emoji = "🎅🤶❄⛄🎄🎁🕯🌟✨🔥🥣🎶🎆👼🦌🛷"
        alphabet_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


        # Connect emoji to alphabet
        print("\n(1) Emoji to alphabet")
        print("Length: " + str(len(alphabet_emoji)))
        print("Emoji\tUnicode\tOccurrence\tLetter")
        counter = Counter(alphabet_emoji)
        replacement_dictionary = dict()
        x = 0
        for emoji in alphabet_emoji:
            unicode = f'U+{ord(emoji):X}'
            occurrence = counter[emoji]
            letter = alphabet_uppercase[x]
            print(emoji + "\t\t" + unicode + "\t\t" + str(occurrence) + "\t\t" + letter)

            # Add to dictionary
            replacement_dictionary[emoji] = str(letter);

            x = x+1


        # Break the code
        print("\n(2) Break the code")
        print("Length: " + str(len(secret_code)))
        print("Emoji\tUnicode\tOccurrence\tReplaced")
        counter = Counter(secret_code)
        x = 0
        solution = ''
        for emoji in secret_code:
            unicode = f'U+{ord(emoji):X}'
            occurrence = counter[emoji]
            replaced_character = replacement_dictionary[emoji]

            print(emoji + "\t\t" + unicode + "\t\t" + str(occurrence) + "\t\t" + replaced_character)

            x=x+1

    def solveCode():
        # Replacement alpabet for 🎅🤶❄⛄🎄🎁🕯🌟✨🔥🥣🎶🎆👼🦌🛷
        replacement_dictionary = dict()
        replacement_dictionary['🎅'] = 'A' #1
        replacement_dictionary['🤶'] = 'B' #2
        replacement_dictionary['❄'] = 'C' #3
        replacement_dictionary['⛄'] = '}' #4 ok
        replacement_dictionary['🎄'] = 'E' #5
        replacement_dictionary['🎁'] = 'F' #6
        replacement_dictionary['🕯'] = 'G' #7
        replacement_dictionary['🌟'] = 'H' #8
        replacement_dictionary['✨'] = 'I' #9
        replacement_dictionary['🔥'] = 'J' #10
        replacement_dictionary['🥣'] = '{' #11 ok
        replacement_dictionary['🎶'] = 'L' #12
        replacement_dictionary['🎆'] = 'M' #13
        replacement_dictionary['👼'] = 'N' #14
        replacement_dictionary['🦌'] = 'O' #15
        replacement_dictionary['🛷'] = 'P' #16




        # Break the code
        secret_code = "🤶🛷✨🎶🎅✨🎅🎅🛷🤶🎄🔥🎆🦌🎁🛷🎅❄🛷🛷🎅🎶🎅✨🎅🦌🥣🔥🛷🦌⛄🎅🌟🛷🛷🔥🎄🦌🎅✨🦌🦌🕯🎶🎅🤶🦌❄🎁🕯🎅✨🎶👼🌟🎆🕯🌟❄👼🎅🎅🤶❄🎄👼🎆🔥🎁🛷🤶👼🎅🎅🎅🎅🎅🎅"
        print("\nBreak with known alphabet")
        counter = Counter(secret_code)
        x = 0
        solution = ''
        for emoji in secret_code:
            unicode = f'U+{ord(emoji):X}'
            occurrence = counter[emoji]
            replaced_character = replacement_dictionary[emoji]

            print(replaced_character, end='')

            x=x+1


    printOverview()
    solveCode()