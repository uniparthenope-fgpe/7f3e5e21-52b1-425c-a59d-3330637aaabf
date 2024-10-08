def sort_fleet(fleet):
    fleet.sort(key=lambda x: x['speed'], reverse=True)
    return fleet