def travel_itinerary(planets, start):
    itinerary = [start]
    for planet in planets:
        itinerary.append(planet)
    itinerary.append(start)  # Return to starting planet
    return itinerary

# Example usage:
print(travel_itinerary(['Tatooine', 'Hoth', 'Endor'], 'Tatooine'))