import random

def generate_droid_name():
    prefixes = ['R2', 'C3', 'BB', 'IG']
    suffixes = ['D2', 'X9', 'T5', 'Q7']
    return random.choice(prefixes) + random.choice(suffixes)
