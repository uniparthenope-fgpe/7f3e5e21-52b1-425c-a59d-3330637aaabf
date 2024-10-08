def encounter_creatures(creatures):
    count = 0
    for creature in creatures:
        if creature == 'Dragon':
            count += 1
    return count

print(encounter_creatures(['Dragon', 'Unicorn', 'Dragon']))