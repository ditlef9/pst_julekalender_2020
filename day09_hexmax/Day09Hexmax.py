# Filename: Day09Hexmax_old.py
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
import binascii
from collections import Counter


class Day09Hexmax:
    print('')
    print('~~~~~~~~~~~~~~~~~~~~~~~~ Day 09 ~~~~~~~~~~~~~~~~~~~~~~~~')


    def breakTheCode():

        # Code to break
        secret_code = "🤶🛷✨🎶🎅✨🎅🎅🛷🤶🎄🔥🎆🦌🎁🛷🎅❄🛷🛷🎅🎶🎅✨🎅🦌🥣🔥🛷🦌⛄🎅🌟🛷🛷🔥🎄🦌🎅✨🦌🦌🕯🎶🎅🤶🦌❄🎁🕯🎅✨🎶👼🌟🎆🕯🌟❄👼🎅🎅🤶❄🎄👼🎆🔥🎁🛷🤶👼🎅🎅🎅🎅🎅🎅"

        # Input
        alphabet_emoji = "🎅🤶❄⛄🎄🎁🕯🌟✨🔥🥣🎶🎆👼🦌🛷"
        alphabet_hex = "0123456789ABCDEF"


        # Connect emoji to alphabet
        print("\n(1) Emoji to alphabet")
        print("Length: " + str(len(alphabet_emoji)))
        print("Emoji\tNumber (Hex)")
        counter = Counter(alphabet_emoji)
        replacement_dictionary = dict()
        x = 0
        for emoji in alphabet_emoji:
            hex = alphabet_hex[x]
            print(emoji + "\t\t" + "\t\t" + str(hex))

            # Add to dictionary
            replacement_dictionary[emoji] = str(hex);

            x = x+1


        # Replace secret_code emoji to hex from alphabet
        print("\n(2) Replace secret code emoji to hex from alphabet")
        print("Length: " + str(len(secret_code)))
        print("Emoji\t\tReplaced with\t\tOccurrence")
        counter = Counter(secret_code)
        x = 0
        solution = ''
        for emoji in secret_code:
            occurrence = counter[emoji]
            replaced_character = replacement_dictionary[emoji]

            print(emoji + "\t\t" + replaced_character + "\t\t" + str(occurrence))
            solution = solution + replaced_character;
            x=x+1


        # Solution to zip
        # 1F8B0800F149CE5F02FF0B080EA9FE307FF94E08EE6B01E25608BD7C672D00124DC95F1D000000
        print("\n\n(3) Hex solution code is:")
        print(solution)
        print("\nCopy the code and open HxD program. Create new file. Paste the code into HxD.")
        print("Save the file as solution.gz. Open solution.gz in WinRar. You now got the solution.")
        print("Google 1F8B08.")



    breakTheCode()