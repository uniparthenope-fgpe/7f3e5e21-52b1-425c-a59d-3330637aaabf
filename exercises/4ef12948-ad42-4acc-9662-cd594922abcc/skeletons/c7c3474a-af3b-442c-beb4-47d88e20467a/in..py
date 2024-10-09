def defense_simulation(spells):
    success_rate = 0
    for spell in spells:
        if spell['type'] == 'defensive':
            success_rate += 1
    return success_rate / len(spells)