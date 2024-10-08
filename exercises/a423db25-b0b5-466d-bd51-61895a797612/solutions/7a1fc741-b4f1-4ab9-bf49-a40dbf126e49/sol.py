import random

def generate_potion(ingredients):
    potion_name = random.choice(['Felix Felicis', 'Polyjuice Potion', 'Amortentia'])
    return potion_name + ' with ' + ', '.join(ingredients)

# Example usage:
ingredients = ['dragon liver', 'unicorn hair', 'moonstone']
print(generate_potion(ingredients))