#
# Dice display ROM
# Multiplexed
#

# 7-segment numbers
#      R7654321
n0 = 0b00111111
n1 = 0b00000110
n2 = 0b01011011
n3 = 0b01001111
n4 = 0b01100110
n5 = 0b01101101
n6 = 0b01111101
n7 = 0b00000111
n8 = 0b01111111
n9 = 0b01101111
# 7-segment dice
d1 = 0b00000001
d2 = 0b00000110
d3 = 0b00000111
d4 = 0b00011110
d5 = 0b00011111
d6 = 0b01111110
d12 = d2  # 0b00010010
d13 = d3  # 0b00010011

rom = [0 for _ in range(8192)]
seq = 0


def patterns(num1, num2, die1, die2):
    global seq, mode
    reset = 128
    a = mode*256 + (seq % 36)
    rom[a] = num1 | reset
    rom[a+64] = num2 | reset
    rom[a+128] = die1 | reset
    rom[a+192] = die2 | reset
    seq += 1


def save_bin(filename):
    print("\nSaving {:s} as binary file".format(filename))
    rom_bin = bytearray()
    for i in range(len(rom)):
        rom_bin.append(rom[i] or 0)
    rom_image = open(filename, "wb")
    rom_image.write(rom_bin)
    rom_image.close()


def dump():
    for i in range(0, len(rom), 8):
        print("{:04X}: {:02X} {:02X} {:02X} {:02X} {:02X} {:02X} {:02X} {:02X}"
              .format(i, rom[i], rom[i+1], rom[i+2], rom[i+3], rom[i+4], rom[i+5], rom[i+6], rom[i+7]))


# Mode 0 = 1 die
mode = 0
patterns(0, n1, 0, d1)
patterns(0, n2, 0, d12)
patterns(0, n3, 0, d13)
patterns(0, n4, 0, d4)
patterns(0, n5, 0, d5)
patterns(0, n6, 0, d6)
patterns(0, n1, 0, d1)
patterns(0, n2, 0, d12)
patterns(0, n3, 0, d13)
patterns(0, n4, 0, d4)
patterns(0, n5, 0, d5)
patterns(0, n6, 0, d6)
patterns(0, n1, 0, d1)
patterns(0, n2, 0, d12)
patterns(0, n3, 0, d13)
patterns(0, n4, 0, d4)
patterns(0, n5, 0, d5)
patterns(0, n6, 0, d6)
patterns(0, n1, 0, d1)
patterns(0, n2, 0, d12)
patterns(0, n3, 0, d13)
patterns(0, n4, 0, d4)
patterns(0, n5, 0, d5)
patterns(0, n6, 0, d6)
patterns(0, n1, 0, d1)
patterns(0, n2, 0, d12)
patterns(0, n3, 0, d13)
patterns(0, n4, 0, d4)
patterns(0, n5, 0, d5)
patterns(0, n6, 0, d6)
patterns(0, n1, 0, d1)
patterns(0, n2, 0, d12)
patterns(0, n3, 0, d13)
patterns(0, n4, 0, d4)
patterns(0, n5, 0, d5)
patterns(0, n6, 0, d6)

# mode 1 = 2 dice - count
mode = 1
patterns(n0, n0, d1, d1)
patterns(n0, n1, d1, d12)
patterns(n0, n2, d1, d13)
patterns(n0, n3, d1, d4)
patterns(n0, n4, d1, d5)
patterns(n0, n5, d1, d6)

patterns(n0, n6, d2, d1)
patterns(n0, n7, d2, d12)
patterns(n0, n8, d2, d13)
patterns(n0, n9, d2, d4)
patterns(n1, n0, d2, d5)
patterns(n1, n1, d2, d6)

patterns(n1, n2, d3, d1)
patterns(n1, n3, d3, d12)
patterns(n1, n4, d3, d13)
patterns(n1, n5, d3, d4)
patterns(n1, n6, d3, d5)
patterns(n1, n7, d3, d6)

patterns(n1, n8, d4, d1)
patterns(n1, n9, d4, d12)
patterns(n2, n0, d4, d13)
patterns(n2, n1, d4, d4)
patterns(n2, n2, d4, d5)
patterns(n2, n3, d4, d6)

patterns(n2, n4, d5, d1)
patterns(n2, n5, d5, d12)
patterns(n2, n6, d5, d13)
patterns(n2, n7, d5, d4)
patterns(n2, n8, d5, d5)
patterns(n2, n9, d5, d6)

patterns(n3, n0, d6, d1)
patterns(n3, n1, d6, d12)
patterns(n3, n2, d6, d13)
patterns(n3, n3, d6, d4)
patterns(n3, n4, d6, d5)
patterns(n3, n5, d6, d6)

# mode 2 = 2 dice no adding
mode = 2
patterns(n1, n1, d1, d1)
patterns(n1, n2, d1, d12)
patterns(n1, n3, d1, d13)
patterns(n1, n4, d1, d4)
patterns(n1, n5, d1, d5)
patterns(n1, n6, d1, d6)

patterns(n2, n1, d2, d1)
patterns(n2, n2, d2, d12)
patterns(n2, n3, d2, d13)
patterns(n2, n4, d2, d4)
patterns(n2, n5, d2, d5)
patterns(n2, n6, d2, d6)

patterns(n3, n1, d3, d1)
patterns(n3, n2, d3, d12)
patterns(n3, n3, d3, d13)
patterns(n3, n4, d3, d4)
patterns(n3, n5, d3, d5)
patterns(n3, n6, d3, d6)

patterns(n4, n1, d4, d1)
patterns(n4, n2, d4, d12)
patterns(n4, n3, d4, d13)
patterns(n4, n4, d4, d4)
patterns(n4, n5, d4, d5)
patterns(n4, n6, d4, d6)

patterns(n5, n1, d5, d1)
patterns(n5, n2, d5, d12)
patterns(n5, n3, d5, d13)
patterns(n5, n4, d5, d4)
patterns(n5, n5, d5, d5)
patterns(n5, n6, d5, d6)

patterns(n6, n1, d6, d1)
patterns(n6, n2, d6, d12)
patterns(n6, n3, d6, d13)
patterns(n6, n4, d6, d4)
patterns(n6, n5, d6, d5)
patterns(n6, n6, d6, d6)

# mode 3 = 2 dice adding
mode = 3
patterns( 0, n2, d1, d1)
patterns( 0, n3, d1, d12)
patterns( 0, n4, d1, d13)
patterns( 0, n5, d1, d4)
patterns( 0, n6, d1, d5)
patterns( 0, n7, d1, d6)

patterns( 0, n3, d2, d1)
patterns( 0, n4, d2, d12)
patterns( 0, n5, d2, d13)
patterns( 0, n6, d2, d4)
patterns( 0, n7, d2, d5)
patterns( 0, n8, d2, d6)

patterns( 0, n4, d3, d1)
patterns( 0, n5, d3, d12)
patterns( 0, n6, d3, d13)
patterns( 0, n7, d3, d4)
patterns( 0, n8, d3, d5)
patterns( 0, n9, d3, d6)

patterns( 0, n5, d4, d1)
patterns( 0, n6, d4, d12)
patterns( 0, n7, d4, d13)
patterns( 0, n8, d4, d4)
patterns( 0, n9, d4, d5)
patterns(n1, n0, d4, d6)

patterns( 0, n6, d5, d1)
patterns( 0, n7, d5, d12)
patterns( 0, n8, d5, d13)
patterns( 0, n9, d5, d4)
patterns(n1, n0, d5, d5)
patterns(n1, n1, d5, d6)

patterns( 0, n7, d6, d1)
patterns( 0, n8, d6, d12)
patterns( 0, n9, d6, d13)
patterns(n1, n0, d6, d4)
patterns(n1, n1, d6, d5)
patterns(n1, n2, d6, d6)

dump()
save_bin('dice.bin')


