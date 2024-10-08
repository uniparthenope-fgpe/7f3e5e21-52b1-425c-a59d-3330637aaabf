def calculate_efficiency(distance, fuel):
    efficiency = distance / fuel
    return efficiency

# Test the function
print(calculate_efficiency(100, 0))  # Should not crash
print(calculate_efficiency(100, 10))  # Should return 10.0