def lightsaber_duel(player1_health, player2_health):
    while player1_health > 0 and player2_health > 0:
        player1_health -= 10
        player2_health -= 10
    if player1_health <= 0:
        return 'Player 2 wins!'
    else:
        return 'Player 1 wins!'