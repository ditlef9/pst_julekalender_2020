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
# Bytes specification:  https://github.com/PSTNorge/slede8/blob/main/src/assembler.ts
#                       https://github.com/PSTNorge/slede8/blob/main/src/runtime.ts
#
from day12_slede8_read_compound_file.Day12Slede8ReadCompoundFileSolve import Day12Slede8ReadCompoundFileSolve


class Day12Slede8ReadCompoundFile:
    print('')
    print('~~~~~~~~~~~~~~~~~~~~~~~~ Day 12 ~~~~~~~~~~~~~~~~~~~~~~~~')
    print('Specification: https://github.com/PSTNorge/slede8/blob/main/src/assembler.ts')
    print('Specification: https://github.com/PSTNorge/slede8/blob/main/src/runtime.ts')



    """ Read File as Hex -------------------------------------------------------- """
    def readFileAsHex():
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
        print("\nx=" + str(x))

        # Print bytes
        print("\n\n(2) Print bytes:")
        bytes_split = bytes.split('\\')
        x = 0
        for byte in bytes_split:
            print(byte, end=" ")
            x = x +1
        print("\nx=" + str(x))

    """ Unslede 8 -------------------------------------------------------- """
    def unslede8():
        print("Reverse engineer program.s8:")
        # label_0x0000:
        # 0000:  51 00  MOV r5, 0x00
        # 0002:  61 01  MOV r6, 0x01
        # 0004:  a1 00  MOV r10, 0x00
        # 0006:  b1 01  MOV r11, 0x01
        # 0008:  c1 00  MOV r12, 0x00
        # 000a:  83 03  FINN 0038
        # 000c:  91 1a  MOV r9, 0x1a
        #
        # label_0x000e:
        # 000e:  06 02  READ r2
        # 0010:  04 03  LOAD r3
        # 0012:  72 05  MOV r7, r5
        # 0014:  55 67  ADD r7, r6  ; .data 'Ug'
        # 0016:  25 72  XOR r2, r7  ; .data '%r'
        # 0018:  25 32  XOR r2, r3  ; .data '%2'
        # 001a:  15 2c  OR r12, r2
        # 001c:  52 06  MOV r5, r6
        # 001e:  62 07  MOV r6, r7
        # 0020:  65 b9  SUB r9, r11
        # 0022:  55 b0  ADD r0, r11
        # 0024:  17 a9  NEQ r9, r10
        # 0026:  e9 00  FJMP 000e
        # 0028:  07 ac  EQ r12, r10
        # 002a:  29 03  FJMP 0032
        # 002c:  b3 05  FINN 005b
        # 002e:  1a 06  CALL 0061
        # 0030:  00 00  HALT
        #
        # label_0x0032:
        # 0032:  23 05  FINN 0052
        # 0034:  1a 06  CALL 0061
        # 0036:  00 00  HALT
        #
        # label_0x0038:
        # 0038:  51 51  MOV r5, 0x51  ; .data 'QQ'
        # 003a:  57 7e  GTE r14, r7  ; .data 'W~'
        # 003c:  .data 6e ('n')
        # 003d:  .data 64 ('d')
        # 003e:  .data 77 ('w')
        # 003f:  .data 12 ('')
        # 0040:  59 38  FJMP 0385  ; .data 'Y8'
        # 0042:  f3 8a  FINN 08af
        # 0044:  48 3d  JMP 03d4  ; .data 'H='
        # 0046:  eb 53  RET
        # 0048:  .data 7d ('}')
        # 0049:  .data 21 ('!')
        # 004a:  5c af  NOP
        # 004c:  1c ae  NOP
        # 004e:  50 25  HALT  ; .data 'P%'
        # 0050:  55 3f  ADD r15, r3  ; .data 'U?'
        #
        # label_0x0052:
        # 0052:  4b 6f  RET  ; .data 'Ko'
        # 0054:  72 72  MOV r7, r2  ; .data 'rr'
        # 0056:  65 6b  SUB r11, r6  ; .data 'ek'
        # 0058:  .data 74 ('t')
        # 0059:  .data 21 ('!')
        # 005a:  00 46  HALT
        # 005c:  65 69  SUB r9, r6  ; .data 'ei'
        # 005e:  6c 21  NOP  ; .data 'l!'
        # 0060:  00 04  HALT
        # 0062:  02 07  MOV r0, r7
        # 0064:  a2 d9  MOV r10, r9
        # 0066:  06 16  READ r6
        # 0068:  02 55  MOV r0, r5
        # 006a:  b0 18  HALT
        # 006c:  06 0b  READ r11
        # 006e:  .data 00 ('')

    """ Strings -------------------------------------------------------- """
    def strings():
        print("Strings program.s8:")
        #.SLEDE8Q
        #Ug%r%2
        #QQW~ndw
        #S}!\
        #P%U?Korrekt!

        # What we need to do now is reverse-engineer logic to "Korrekt!"

        # 0034:  1a 06  CALL 0061

    """ Reverse engineer -------------------------------------------------------- """
    def reverseEngineer():
        print("Reverse Engineer program.s8:")

        # label_0x0000:
        # 0000:  51 00  MOV r5, 0x00
        # 0002:  61 01  MOV r6, 0x01
        # 0004:  a1 00  MOV r10, 0x00
        # 0006:  b1 01  MOV r11, 0x01
        # 0008:  c1 00  MOV r12, 0x00
        # 000a:  83 03  FINN 0038
        # 000c:  91 1a  MOV r9, 0x1a
        #
        # label_0x000e:
        # 000e:  06 02  READ r2
        # 0010:  04 03  LOAD r3
        # 0012:  72 05  MOV r7, r5
        # 0014:  55 67  ADD r7, r6  ; .data 'Ug'
        # 0016:  25 72  XOR r2, r7  ; .data '%r'
        # 0018:  25 32  XOR r2, r3  ; .data '%2'
        # 001a:  15 2c  OR r12, r2
        # 001c:  52 06  MOV r5, r6
        # 001e:  62 07  MOV r6, r7
        # 0020:  65 b9  SUB r9, r11
        # 0022:  55 b0  ADD r0, r11
        # 0024:  17 a9  NEQ r9, r10
        # 0026:  e9 00  FJMP 000e
        # 0028:  07 ac  EQ r12, r10
        # 002a:  29 03  FJMP 0032
        # 002c:  b3 05  FINN 005b
        # 002e:  1a 06  CALL 0061

        # MACIG
        # label_0x0061:
        # 0061:  04 02  LOAD r2
        # 0063:  07 a2  EQ r2, r10
        # 0065:  d9 06  FJMP 006d
        # 0067:  16 02  WRITE r2
        # 0069:  55 b0  ADD r0, r11
        # 006b:  18 06  JMP 0061
        #
        # label_0x006d:
        # 006d:  0b 00  RET
        # 000a:  83 03  FINN 0038
        # 0x38 is the magic offset

        # xor-ish challegende. Do XOR
        # Fibonacci sequence

    """ Scriptstart ---------------------------------------------------------- """
    # Reverse engineer code
    readFileAsHex()
    unslede8()
    strings()
    reverseEngineer()

    # Solve
    day12Slede8ReadCompoundFileSolve = Day12Slede8ReadCompoundFileSolve()
    day12Slede8ReadCompoundFileSolve.solve()