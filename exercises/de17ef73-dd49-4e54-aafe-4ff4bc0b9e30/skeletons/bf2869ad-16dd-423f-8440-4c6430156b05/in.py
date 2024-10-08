def cast_spell(spell):
    try:
        if spell == 'Expelliarmus':
            return 'Disarming Spell'
        elif spell == 'Avada Kedavra':
            return 'Killing Curse'
        else:
            raise ValueError('Unknown Spell')
    except ValueError as e:
        return str(e)