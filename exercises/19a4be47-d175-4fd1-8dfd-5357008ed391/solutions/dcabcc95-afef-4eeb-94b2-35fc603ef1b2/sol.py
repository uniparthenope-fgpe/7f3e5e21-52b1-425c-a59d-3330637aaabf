def total_force_power(jedi_count, sith_count):
    total_power = 0
    for i in range(jedi_count):
        total_power += 2
    for j in range(sith_count):
        total_power += 3
    return total_power

# Example usage:
print(total_force_power(3, 2))  # Expected output: 12