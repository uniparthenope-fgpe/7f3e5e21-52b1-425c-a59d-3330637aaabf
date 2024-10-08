import random

def generate_potion(ingredients):
    potion_name = random.choice(['Felix Felicis', 'Polyjuice Potion', 'Amortentia'])
    return potion_name + ' with ' + ', '.join(ingredients)