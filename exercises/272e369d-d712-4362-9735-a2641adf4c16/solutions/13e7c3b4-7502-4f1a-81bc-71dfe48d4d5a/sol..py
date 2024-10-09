def calculate_score(goals, penalties):
    score = (goals * 10) - (penalties * 5)
    return score