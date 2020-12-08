# Filename: Day08ASN1.py
# Author: S Ditlefsen
# License: http://opensource.org/licenses/gpl-license.php GNU Public License

# Assignment:
#   Det er viktig med faglig utvikling, også nå i førjulsstria. Dagens tema er ASN.1. Her er litt hjernetrim fra Nissens Kompetansebank™.
#
# MIIBOTCCATAwggEnMIIBHjCCARUwggEMMIIBAzCB+zCB8zCB6zCB4zCB2zCB0zCByzCBwzCBuzCBszCBqzCBozCBnDCBlDCBjDCBhDB9MHYwbzBoMGEwWjBTMEwwRTA+MDcwMTAqMCMwHDAVMA4wBwUAoQMCAROgAwIBA6EDAgEMogMCAQChAwIBE6ADAgEBoQMCARKkAgUAoQMCARShAwIBDqIDAgEYoQMCAQShAwIBEqEDAgEOoQMCAQ6hAwIBB6IDAgECogMCAQigAwIBAaIDAgENogMCARKiAwIBAKMCBQCiAwIBE6IDAgESogMCAQ+hAwIBEaEDAgEOoQMCAQugAwIBAKIDAgEDoQMCAQyhAwIBFKEDAgESoQMCAQ+gAwIBAaEDAgEMoAMCAQOhAwIBEaEDAgEOogMCAQs=

class Day08ASN1:
    print('')
    print('~~~~~~~~~~~~~~~~~~~~~~~~ Day 08 ~~~~~~~~~~~~~~~~~~~~~~~~')

    # About today
    print("Todays assignment was a ASN.1 signal. It needs to be converted to readable text.")
    print("I used https://holtstrom.com/michael/tools/asn1decoder.php for this purpose.")
    print("Signal = MIIBOTCCATAwggEnMIIBHjCCARUwggEMMIIBAzCB+zCB8zCB6zCB4zCB2zCB0zCByzCBwzCBuzCBszCBqzCBozCBnDCBlDCBjDCBhDB9MHYwbzBoMGEwWjBTMEwwRTA+MDcwMTAqMCMwHDAVMA4wBwUAoQMCAROgAwIBA6EDAgEMogMCAQChAwIBE6ADAgEBoQMCARKkAgUAoQMCARShAwIBDqIDAgEYoQMCAQShAwIBEqEDAgEOoQMCAQ6hAwIBB6IDAgECogMCAQigAwIBAaIDAgENogMCARKiAwIBAKMCBQCiAwIBE6IDAgESogMCAQ+hAwIBEaEDAgEOoQMCAQugAwIBAKIDAgEDoQMCAQyhAwIBFKEDAgESoQMCAQ+gAwIBAaEDAgEMoAMCAQOhAwIBEaEDAgEOogMCAQs=")

    print("\n")
    print("Now look at ASN.1 spec. It specified that each SEQUENCE either can be;")
    print("[0] digit")
    print("[1] lower case alphabet")
    print("[2] upper case alphabet")
    print("[3] leftCurlyBracket")
    print("[3] rightCurlyBracket")
    print("\n")
    print("Use the convertion table printed below to convert each SEQUENCE, example ")
    print("[1] {INTEGER 0x13 (19 decimal) } is lower case alphabet index 19 which is t.")
    print("[0] {INTEGER 0x03 (3 decimal) } is lower digit index 3 which is 3.")

    # Print alphabet and digits
    digits = '123456789'
    alphabet_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    print("[0] DIGITS:")
    x=1;
    for digit in digits:
        print(str(x) + ": " + digit + "  ", end='')
        x=x+1

    print("\n[1] Alphabet lowercase:")
    x=0;
    for char in alphabet_lowercase:
        print(str(x) + ": " + char + "  ", end='')
        x=x+1

    print("\n[2] Alphabet uppercase:")
    x = 0;
    for char in alphabet_uppercase:
        print(str(x) + ": " + char + "  ", end='')
        x = x + 1