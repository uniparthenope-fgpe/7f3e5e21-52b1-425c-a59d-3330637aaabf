def lightsaber_duel(player1_health, player2_health):
    while player1_health > 0 and player2_health > 0:
        player1_health -= 10
        player2_health -= 10
    return 'Duel Over!'