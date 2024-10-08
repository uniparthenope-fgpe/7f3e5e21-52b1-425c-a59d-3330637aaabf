import random

def generate_droid_name():
    adjectives = ['R2', 'BB', 'C3']
    nouns = ['D2', 'Q5', 'X9']
    return random.choice(adjectives) + random.choice(nouns)