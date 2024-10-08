def sort_starships(starships):
    return sorted(starships, key=lambda x: x['speed'])

starships = [{'name': 'X-Wing', 'speed': 1050}, {'name': 'TIE Fighter', 'speed': 1200}]
sorted_starships = sort_starships(starships)
print(sorted_starships)