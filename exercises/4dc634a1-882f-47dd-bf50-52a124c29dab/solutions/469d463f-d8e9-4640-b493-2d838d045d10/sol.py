class QuidditchMatch:
    def __init__(self):
        self.goals = 0
        self.fouls = 0

    def score_goal(self):
        self.goals += 1

    def commit_foul(self):
        self.fouls += 1

    def get_score(self):
        return self.goals, self.fouls

match = QuidditchMatch()
match.score_goal()
match.commit_foul()
print(match.get_score())