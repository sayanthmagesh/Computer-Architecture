
def binary(n):
    return format(n & 255, '08b')

def add(a, b):
    a_bin = binary(a)
    b_bin = binary(b)

    total = int(a_bin, 2) + int(b_bin, 2)
    result_bin = binary(total)
    result = int(result_bin, 2)

    if result >= 128:
        result -= 256

    overflow = (a >= 0 and b >= 0 and result < 0) or \
               (a < 0 and b < 0 and result >= 0)

    print(a_bin, "+", b_bin)
    print("Result =", result_bin)
    print("Decimal =", result)
    


# a) 45 - (+19) = 45 + (-19)
print("a) 45 - (+19)")
print("45  =", binary(45))
print("+19 =", binary(19))
print("-19 =", binary(-19))
add(45, -19)

# b) (-35) - (-12) = (-35) + 12
print("\nb) (-35) - (-12)")
print("-35 =", binary(-35))
print("-12 =", binary(-12))
print("+12 =", binary(12))
add(-35, 12)
