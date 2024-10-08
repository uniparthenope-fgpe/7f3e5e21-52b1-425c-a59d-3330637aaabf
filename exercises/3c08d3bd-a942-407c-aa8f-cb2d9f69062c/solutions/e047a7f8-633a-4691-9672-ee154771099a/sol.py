import random

class Participant:
    def __init__(self, name):
        self.name = name
        self.score = 0

class Tournament:
    def __init__(self):
        self.participants = []

    def add_participant(self, participant):
        self.participants.append(participant)

    def conduct_challenge(self):
        for participant in self.participants:
            participant.score += random.randint(1, 10)

    def get_winner(self):
        return max(self.participants, key=lambda p: p.score)