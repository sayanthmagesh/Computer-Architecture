def rotate_right_without_carry(binary_str, positions=3):
  """Performs Rotate Right without carry (ROR) step by step."""
  print(f"Initial binary: {binary_str}")
  bits = list(binary_str)
  
  for step in range(1, positions + 1):
    wrapped_bit = bits.pop()
    bits.insert(0, wrapped_bit)
    current_result = "".join(bits)
    print(f"Step {step}: Rotated bit '{wrapped_bit}' from right to left -> {current_result}")
    
  return "".join(bits)

def rotate_right_with_carry(binary_str, carry_flag, positions=3):
  """Performs Rotate Right with carry (RCR) step by step (9-bit total: 8 bits + carry)."""
  print(f"Initial binary: {binary_str}, Initial Carry Flag: {carry_flag}")
  bits = list(binary_str)
  c = carry_flag
  
  for step in range(1, positions + 1):
    old_c = c
    c = bits.pop()
    bits.insert(0, old_c)
    current_result = "".join(bits)
    print(f"Step {step}: Carry becomes '{c}', leftmost bit becomes old carry '{old_c}' -> Result: {current_result} | Carry: {c}")
    
  return "".join(bits), c

def main():
  print("=== a) Rotate Right Without Carry (ROR) ===")
  bin_a = "11011101"
  final_a = rotate_right_without_carry(bin_a, positions=3)
  print(f"Final ROR Result: {final_a}\n")
  
  print("=== b) Rotate Right With Carry (RCR) ===")
  bin_b = "11010000"
  initial_carry = "1"
  final_b, final_carry = rotate_right_with_carry(bin_b, initial_carry, positions=3)
  print(f"Final RCR Result: {final_b}, Final Carry Flag: {final_carry}")

if __name__ == "__main__":
  main()