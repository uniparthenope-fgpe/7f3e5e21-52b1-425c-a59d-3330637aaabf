def travel_time(distance, speed):
    if speed <= 0:
        return 'Speed must be greater than zero'
    return distance / speed