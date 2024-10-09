class Champion:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores
    def average_score(self):
        return sum(self.scores) / len(self.scores)