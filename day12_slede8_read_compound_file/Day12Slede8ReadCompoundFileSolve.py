


class Day12Slede8ReadCompoundFileSolve:

    def solve(self):
        ct = (
            0x51, 0x51, 0x57, 0x7e, 0x6e, 0x64, 0x77,
            0x12, 0x59, 0x38, 0xf3, 0x8a, 0x48, 0x3d,
            0xeb, 0x53, 0x7d, 0x21, 0x5c, 0xaf, 0x1c,
            0xae, 0x50, 0x25, 0x55, 0x3f,
        )

        r5, r6 = 0, 1
        res = ''
        for i, c in enumerate(ct):
            key = 0
            r7 = (r5 + r6) & 0xff
            key ^= r7
            key ^= c
            r5 = r6
            r6 = r7
            res += chr(key)

        print(res)