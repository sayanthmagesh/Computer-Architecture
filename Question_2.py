

num = 0b10110110

print("a) ROL by 2 positions")
print("Original =", format(num, '08b'))

for i in range(2):
    msb = (num >> 7) & 1
    num = ((num << 1) & 255) | msb
    print("Step", i + 1, "=", format(num, '08b'))

print("Final Result =", format(num, '08b'))

num = 0b10110110
carry = 0

print("\nb) RCL by 2 positions")
print("Original =", format(num, '08b'))
print("Initial Carry =", carry)

for i in range(2):
    msb = (num >> 7) & 1
    num = ((num << 1) & 255) | carry
    carry = msb
    print("Step", i + 1, "=", format(num, '08b'),
          "Carry =", carry)

print("Final Result =", format(num, '08b'))
print("Final Carry =", carry)
