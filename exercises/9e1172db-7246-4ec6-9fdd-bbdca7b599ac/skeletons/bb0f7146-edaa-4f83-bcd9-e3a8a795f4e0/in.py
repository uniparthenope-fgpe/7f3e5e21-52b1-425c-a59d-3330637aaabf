def spell_checker(words):
    corrected = []
    for word in words:
        if word == 'alohomora':
            corrected.append('Alohomora')
        else:
            corrected.append(word)
    return corrected