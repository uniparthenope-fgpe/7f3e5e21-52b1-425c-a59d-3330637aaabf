def duel(spell):
    if spell == 'Expelliarmus':
        return 'Basilisk disarmed!'
    elif spell == 'Stupefy':
        return 'Basilisk stunned!'
    elif spell == 'Avada Kedavra':
        return 'Basilisk defeated!'
    else:
        return 'Invalid spell!'

# Example usage:
result = duel('Expelliarmus')
print(result)