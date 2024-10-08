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

# Example usage:
tournament = Tournament()
tournament.add_participant(Participant('Harry'))