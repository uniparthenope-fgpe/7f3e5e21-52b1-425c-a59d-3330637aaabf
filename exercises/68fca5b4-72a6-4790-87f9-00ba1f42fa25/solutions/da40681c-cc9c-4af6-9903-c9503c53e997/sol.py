class GalacticBattle:
    def __init__(self):
        self.battles = []

    def add_battle(self, winner):
        self.battles.append(winner)

    def get_winner(self):
        return max(set(self.battles), key=self.battles.count)