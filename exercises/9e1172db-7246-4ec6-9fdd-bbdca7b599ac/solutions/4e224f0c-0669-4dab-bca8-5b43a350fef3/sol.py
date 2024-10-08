def spell_checker(words):
    corrected = []
    for word in words:
        if word == 'alohomora':
            corrected.append('Alohomora')
        elif word == 'expelliarmus':
            corrected.append('Expelliarmus')
        else:
            corrected.append(word)
    return corrected