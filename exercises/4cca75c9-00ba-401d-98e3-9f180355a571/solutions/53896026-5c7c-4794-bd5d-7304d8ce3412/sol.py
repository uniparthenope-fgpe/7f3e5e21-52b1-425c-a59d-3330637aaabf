def calculate_speed(distance, time):
    return distance / time

distance = 1000  # in light-years
 time = 5  # in years
print('Starship speed: ' + str(calculate_speed(distance, time)) + ' light-years/year')