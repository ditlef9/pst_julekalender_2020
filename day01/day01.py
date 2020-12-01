# Filename: day01.py
# Author: S D
# License: http://opensource.org/licenses/gpl-license.php GNU Public License

# About class:
#   This class should do ROT24 on a string
#
#   Examples:
#       A -> Y
#       a -> y
#       B -> Z
#       b -> z
#
# Special characters like { and } should not change

# Assignment:
#   Velkommen til DASS
#
#   Hei,
#
#   Kan du bekrefte at du har fått tilgang til systemet? Det gjør du ved å svare på denne meldingen med verifiseringskoden RUV{JgkJqPåGtFgvLwnKilgp}.
#
#   OBS: Jeg mistet verifiseringskoden din i salaten, så mulig du må rette opp i den før du svarer.
#
#   Vennlig hilsen din nærmeste leder

class Day01:
    print('')
    print('~~~~~~~~~~~~~~~~~~~~~~~~ Day 01 ~~~~~~~~~~~~~~~~~~~~~~~~')

    access_code = 'RUV{JgkJqPåGtFgvLwnKilgp}'
    alphabeth_lowercase = 'abcdefghijklmnopqrstuvwxyzæøå'
    alphabeth_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ'
    solution = "";

    for access_code_character in access_code:
        character_found_in_lowercase_or_uppercase = "false";

        # Lowercase find character number, a=1, b=2, c=3 etc
        x = 0;
        for find_char in alphabeth_lowercase:
            x = x+1
            if(find_char == access_code_character):
                switch_with_number = (x + 26) % len(alphabeth_lowercase)
                new_char = alphabeth_lowercase[switch_with_number]
                print("Char " + str(access_code_character) + " -> " + str(new_char) + " -- char number " + str(x) + " in alpabeth, switch with number " + str(switch_with_number))

                solution = solution + str(new_char)
                character_found_in_lowercase_or_uppercase = "true";


        # Uppercase find character number, A=1, B=2, C=3 etc
        x = 0;
        for find_char in alphabeth_uppercase:
            x = x+1
            if(find_char == access_code_character):
                switch_with_number = (x + 26) % len(alphabeth_uppercase)
                new_char = alphabeth_uppercase[switch_with_number]
                print("Char " + str(access_code_character) + " -> " + str(new_char) + " -- char number " + str(x) + " in alpabeth, switch with number " + str(switch_with_number))

                solution = solution + str(new_char)
                character_found_in_lowercase_or_uppercase = "true";

        # Special characters
        if(character_found_in_lowercase_or_uppercase == "false"):
            print("Char " + str(access_code_character) + " -> " + str(access_code_character))

            solution = solution + str(access_code_character)


    print("Solution")
    print(str(access_code))
    print(str(solution))
