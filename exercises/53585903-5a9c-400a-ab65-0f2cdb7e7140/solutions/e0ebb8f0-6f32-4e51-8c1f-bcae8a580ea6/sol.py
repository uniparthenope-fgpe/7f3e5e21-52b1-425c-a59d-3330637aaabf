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

# 1. Create players
player1 = Player('Harry')
player2 = Player('Ron')

# 2. Add players to game
game = Game()
game.add_player(player1)
game.add_player(player2)

# 3. Score goals
game.score_goal(player1)