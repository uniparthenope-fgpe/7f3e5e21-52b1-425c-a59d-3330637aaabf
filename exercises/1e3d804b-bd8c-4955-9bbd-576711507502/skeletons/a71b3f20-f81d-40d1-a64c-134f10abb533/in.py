def calculate_score(goals, fouls):
    score = goals * 10 - fouls * 5
    return score

# Example usage:
print(calculate_score(3, 1)) # Should return 25