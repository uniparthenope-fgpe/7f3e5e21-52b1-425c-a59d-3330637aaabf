class Team:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def score_points(self, points):
        self.score += points

# Example usage:
team1 = Team('Gryffindor')
team1.score_points(10)
print(team1.score)  # Output: 10