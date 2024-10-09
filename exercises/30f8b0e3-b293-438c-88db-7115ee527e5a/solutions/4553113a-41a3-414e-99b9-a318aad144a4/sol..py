def detect_dark_arts(spells):
    dark_arts = []
    for spell in spells:
        if spell in ['Avada Kedavra', 'Crucio']:
            dark_arts.append(spell)
    return dark_arts