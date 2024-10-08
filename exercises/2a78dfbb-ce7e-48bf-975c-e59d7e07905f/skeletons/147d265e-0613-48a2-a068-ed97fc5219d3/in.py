def basilisk_strategy(weaknesses):
    # The original logic is flawed, fix it
    if 'venom' in weaknesses:
        return 'Use the sword'
    elif 'gaze' in weaknesses:
        return 'Use a mirror'
    else:
        return 'Run away'