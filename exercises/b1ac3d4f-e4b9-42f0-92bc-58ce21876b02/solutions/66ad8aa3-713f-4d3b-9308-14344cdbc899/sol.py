def calculate_efficiency(distance, fuel):
    if fuel == 0:
        return 'Fuel cannot be zero!'
    efficiency = distance / fuel
    return efficiency

# Test the function
print(calculate_efficiency(100, 0))  # Should return 'Fuel cannot be zero!'
print(calculate_efficiency(100, 10))  # Should return 10.0