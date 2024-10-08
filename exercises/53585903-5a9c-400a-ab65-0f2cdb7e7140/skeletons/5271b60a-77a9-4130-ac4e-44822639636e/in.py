class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

class Game:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def score_goal(self, player):
        player.score += 10

# Sort the following blocks to complete the game logic
# 1. Create players
# 2. Add players to game
# 3. Score goals
