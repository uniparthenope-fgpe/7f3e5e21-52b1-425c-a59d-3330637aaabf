def jedi_power(training_level):
    if training_level > 3:
        return training_level ** 3  # Corrected to cube the level for higher training
    return training_level ** 2

print(jedi_power(5))  # Expected output: 125