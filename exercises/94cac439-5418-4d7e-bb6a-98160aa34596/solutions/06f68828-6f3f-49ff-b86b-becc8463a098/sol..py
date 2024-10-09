creatures = [('Basilisk', 5), ('Hippogriff', 3), ('Niffler', 1)]
creatures.sort(key=lambda x: x[1])
print(creatures)  # Should print sorted list based on danger level