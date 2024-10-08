def classify_creature(creature):
    if creature == 'Dragon':
        return 'Fire'
    elif creature == 'Unicorn':
        return 'Magical'
    else:
        return 'Unknown'

print(classify_creature('Phoenix'))