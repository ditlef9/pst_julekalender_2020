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

        # Solution

        solution = solution + replaced_character;

        x=x+1

    # Solution
    print("\n(3) Solution=" + solution)