def cast_spell(spell):
    try:
        if spell not in ['Expelliarmus', 'Stupefy']:
            raise ValueError('Invalid spell')
        return 'Spell cast successfully'
    except ValueError:
        return 'Spell failed'