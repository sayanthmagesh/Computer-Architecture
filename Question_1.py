def to_twos_complement(value, bits=8):
  """Converts an integer to its 2's complement binary string of given bits."""
  if value < 0:
    value = (1 << bits) + value
  return format(value & ((1 << bits) - 1), f"0{bits}b")


def from_twos_complement(binary_str):
  """Converts an 2's complement binary string back to a signed integer."""
  bits = len(binary_str)
  value = int(binary_str, 2)
  if binary_str[0] == "1":
    value -= 1 << bits
  return value


def perform_operation(a, b, op):
  """Performs signed binary arithmetic using 8-bit 2's complement logic."""
  bits = 8
  max_val = (1 << (bits - 1)) - 1
  min_val = -(1 << (bits - 1))

  if op == "+":
    decimal_result = a + b
  elif op == "-":
    decimal_result = a - b
  else:
    raise ValueError("Unsupported operator")

  overflow = decimal_result > max_val or decimal_result < min_val

  if op == "+":
    raw_sum = a + b
  else:
    raw_sum = a - b

  binary_result = to_twos_complement(raw_sum, bits)
  final_decimal = from_twos_complement(binary_result)

  return {
      "bin_a": to_twos_complement(a, bits),
      "bin_b": to_twos_complement(b, bits),
      "bin_result": binary_result,
      "decimal_result": final_decimal,
      "overflow": overflow,
  }


def main():
  expressions = [
      (56, 29, "+", "+56 + (+29)"),
      (-38, -23, "-", "(-38) - (-23)"),
  ]

  for a, b, op, desc in expressions:
    print(f"--- Expression: {desc} ---")
    res = perform_operation(a, b, op)

    print(f"Operand A ({a}): {res['bin_a']}")
    print(f"Operand B ({b}): {res['bin_b']}")
    print(f"Binary Result:   {res['bin_result']}")
    print(f"Decimal Result:  {res['decimal_result']}")
    print(f"Overflow:        {'Yes' if res['overflow'] else 'No'}\n")


if __name__ == "__main__":
  main()