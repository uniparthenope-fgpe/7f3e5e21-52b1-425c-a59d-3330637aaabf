def calculate_damage(attack_power, defense_level):
    damage = attack_power - defense_level
    return max(damage, 0)