import math

def convert_coordinates(x, y):
    distance = math.sqrt(x**2 + y**2)
    return distance

# Example usage
print(convert_coordinates(3, 4))  # Should return 5.0