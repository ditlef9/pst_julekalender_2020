
# This class should do ROT24

class Day01:
    print('Day 01')

    access_code = 'AaBbRUV{JgkJqPåGtFgvLwnKilgp}'
    alphabeth_lowercase = 'abcdefghijklmnopqrstuvwxyzæøå'
    alphabeth_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ'

    for access_code_character in access_code:
        # Lowercase find character number, a=1, b=2, c=3 etc
        x = 0;
        for find_char in alphabeth_lowercase:
            x = x+1
            if(find_char == access_code_character):
                print("Char " + str(access_code_character) + " is number " + str(x) + " in alpabeth")

                switch_with_number = x+24

