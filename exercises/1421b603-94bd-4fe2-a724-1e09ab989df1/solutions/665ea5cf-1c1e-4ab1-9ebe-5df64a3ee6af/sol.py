def sort_inventory(items):
    # Sort items based on value
    sorted_items = sorted(items, key=lambda x: x['value'])
    return sorted_items