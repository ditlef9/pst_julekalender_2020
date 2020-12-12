# Filename: day01_rot24.py
# Author: S Ditlefsen
# License: http://opensource.org/licenses/gpl-license.php GNU Public License

# About class:
#   This class should do ROT13 on first letter, rot14 on next etc
#
#   Examples:
#       A -> Y
#       a -> y
#       B -> Z
#       b -> z
#       C -> A
#       C -> a
#       D -> B
#       D -> b
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

class Easter01Rot13Shift:
    print('')
    print('~~~~~~~~~~~~~~~~~~~~~~~~ Easter 01 Day 01 Rot 13 Shift ~~~~~~~~~~~~~~~~~~~~~~~~')



    access_code = 'RUV{JgkJqPåGtFgvLwnKilgp}'
    alphabeth_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    alphabeth_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    solution = "";


    for_counter = 0
    shift_counter = 12;
    for access_code_character in access_code:
        character_found_in_lowercase_or_uppercase = "false";

        # Lowercase find character number, a=1, b=2, c=3 etc
        x = 0;
        for find_char in alphabeth_lowercase:
            x = x+1
            if(find_char == access_code_character):
                switch_with_number = (x + shift_counter) % len(alphabeth_lowercase)
                new_char = alphabeth_lowercase[switch_with_number]
                print("Char " + str(access_code_character) + " -> " + str(new_char) + " -- char number " + str(x) + " in alpabeth, switch with number " + str(switch_with_number) + " " + str(new_char))

                solution = solution + str(new_char)
                character_found_in_lowercase_or_uppercase = "true";


        # Uppercase find character number, A=1, B=2, C=3 etc
        x = 0;
        for find_char in alphabeth_uppercase:
            x = x+1
            if(find_char == access_code_character):
                switch_with_number = (x + shift_counter) % len(alphabeth_uppercase)
                new_char = alphabeth_uppercase[switch_with_number]
                print("Char " + str(access_code_character) + " -> " + str(new_char) + " -- char number " + str(x) + " in alpabeth, switch with number " + str(switch_with_number) + " " + str(new_char))

                solution = solution + str(new_char)
                character_found_in_lowercase_or_uppercase = "true";

        # Special characters
        if(character_found_in_lowercase_or_uppercase == "false"):
            print("Char " + str(access_code_character) + " -> " + str(access_code_character))

            solution = solution + str(access_code_character)


        shift_counter=shift_counter-1

        print("shift_counter=" + str(shift_counter))

        if(shift_counter == 4):
            shift_counter = 12
            print("RESET")

    print("Solution")
    print(str(access_code))
    print(str(solution))
