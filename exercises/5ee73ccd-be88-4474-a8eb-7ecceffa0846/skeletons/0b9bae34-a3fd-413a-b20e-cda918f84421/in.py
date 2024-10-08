class Team:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def score_points(self, points):
        self.score += points

# Sort the blocks to simulate a match