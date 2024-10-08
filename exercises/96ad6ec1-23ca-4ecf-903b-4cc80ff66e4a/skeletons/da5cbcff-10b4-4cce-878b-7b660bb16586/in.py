def calculate_power(dark_energy):
    try:
        power = 10 / dark_energy
        return power
    except ZeroDivisionError:
        return 'Dark energy level cannot be zero!'

print(calculate_power(0))