# Filename: Day12Slede8ReadCompoundFile.py
# Author: S Ditlefsen
# License: http://opensource.org/licenses/gpl-license.php GNU Public License

# Assignment:
#   Det rapporteres at SydpolarSikkerhetstjeneste (SPST) i starten av desember hadde publisert s8asm-kode fra sin GitHub-bruker. Dette ble raskt fjernet, men din kollega Tastefinger rakk å sikre kildekoden.
#
#   Vi stiller oss spørrende til hvordan de har fått tak i spesifikasjonen til dette språket. HR følger opp hvem som har sluttet ila det siste året, og hvorvidt noen av disse kan ha delt denne informasjonen til SPST.
#
#   I mellomtiden har jeg jobbet iherdig med å montere koden. Klarer du å forstå hva SPST vil med dette? Jeg ser frem til verdifull input fra deg!
#
#   Se vedlagt fil for den monterte koden. Tastefinger mente det var relevant å fortelle at du kan finne nyttige verktøy her:
#   https://github.com/PSTNorge/slede8
#
# Bytes specification: https://github.com/PSTNorge/slede8/blob/main/src/assembler.ts
#

class Day12Slede8ReadCompoundFile:
    print('')
    print('~~~~~~~~~~~~~~~~~~~~~~~~ Day 12 ~~~~~~~~~~~~~~~~~~~~~~~~')
    print('Specification: https://github.com/PSTNorge/slede8/blob/main/src/assembler.ts')

    # Read file as hex
    read_file = repr(open("./day12_slede8_read_compound_file/program.s8", 'rb').read())


    # Print file
    print("\n\n(1) Read file:")
    start_offset = 8
    bytes = ""
    x = 0
    for char in read_file:

        if(start_offset < x):
            print(char, end="")
            char = char.replace("x", "")
            bytes = bytes + char;
        x = x +1

    # Print bytes
    print("\n\n(2) Print bytes:")
    bytes_split = bytes.split('\\')
    for byte in bytes_split:
        print(byte, end=" ")