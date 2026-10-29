def to_binary_8bit(val: int) -> str:
    return f"{val & 0xFF:08b}"
def logical_left_shift_8bit(bin_str: str, positions: int = 2):
    print(f"--- Logical Left Shift (<< {positions}) ---")
    print(f"Initial 8-bit Binary: {bin_str} (Decimal: {int(bin_str, 2)})")
    current = bin_str
    for step in range(1, positions + 1):
        discarded_msb = current[0]
        current = current[1:] + "0"
        print(f"Step {step}: Discard MSB '{discarded_msb}', Append '0' at LSB -> {current} (Decimal: {int(current, 2)})")
    print(f"Final 8-bit Result:   {current} (Decimal: {int(current, 2)})\n")
    return current
def logical_right_shift_8bit(bin_str: str, positions: int = 2):
    print(f"--- Logical Right Shift (>> {positions}) ---")
    print(f"Initial 8-bit Binary: {bin_str} (Decimal: {int(bin_str, 2)})")
    current = bin_str
    for step in range(1, positions + 1):
        discarded_lsb = current[-1]
        current = "0" + current[:-1]
        print(
            f"Step {step}: Discard LSB '{discarded_lsb}', Prepend '0' at MSB -> {current} (Decimal: {int(current, 2)})"
        )

    print(f"Final 8-bit Result:   {current} (Decimal: {int(current, 2)})\n")
    return current
print("================ 8-BIT SHIFT OPERATIONS ================\n")
res_a = logical_left_shift_8bit("10110110", 2)
res_b = logical_right_shift_8bit("11010100", 2)
