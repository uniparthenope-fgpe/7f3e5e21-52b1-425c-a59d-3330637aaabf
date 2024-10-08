def droid_production(resources):
    count = 0
    for i in range(resources):
        if i % 2 == 0:
            count += 1
    return count

# Example usage:
print(droid_production(10))  # Expected output: 5