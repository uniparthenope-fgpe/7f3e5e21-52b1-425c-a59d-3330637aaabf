def encounter_creatures(creatures):
    count = 0
    creature_types = {}
    for creature in creatures:
        if creature in creature_types:
            creature_types[creature] += 1
        else:
            creature_types[creature] = 1
    return creature_types

print(encounter_creatures(['Dragon', 'Unicorn', 'Dragon']))