def sort_starships(starships):
    # Sort the starships based on speed
    return sorted(starships, key=lambda x: x[1])