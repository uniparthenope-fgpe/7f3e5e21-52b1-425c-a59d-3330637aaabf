def basilisk_strategy(weaknesses):
    if 'venom' in weaknesses:
        return 'Use the sword'
    elif 'gaze' in weaknesses:
        return 'Use a mirror'
    elif 'speed' in weaknesses:
        return 'Outrun it'
    else:
        return 'Run away'