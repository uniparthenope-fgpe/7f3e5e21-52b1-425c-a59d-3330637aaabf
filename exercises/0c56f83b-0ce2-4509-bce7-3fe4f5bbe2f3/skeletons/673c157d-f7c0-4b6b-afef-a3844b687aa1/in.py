def calculate_score(goals, catches):
    total_score = goals * 10 + catches * 150
    return total_score

# Example usage
print(calculate_score(3, 2))  # Should return 360
