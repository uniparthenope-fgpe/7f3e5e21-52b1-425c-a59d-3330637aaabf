# Define Participant class
class Participant:
    def __init__(self, name):
        self.name = name
        self.points = 0

# Define Tournament class
class Tournament:
    def __init__(self):
        self.participants = []

    def add_participant(self, participant):
        self.participants.append(participant)

    def award_points(self, participant_name, points):
        for participant in self.participants:
            if participant.name == participant_name:
                participant.points += points

    def get_winner(self):
        return max(self.participants, key=lambda p: p.points)

# Example usage:
tournament = Tournament()
tournament.add_participant(Participant('Harry'))
tournament.add_participant(Participant('Cedric'))
tournament.award_points('Harry', 10)
tournament.award_points('Cedric', 5)
print(tournament.get_winner().name)