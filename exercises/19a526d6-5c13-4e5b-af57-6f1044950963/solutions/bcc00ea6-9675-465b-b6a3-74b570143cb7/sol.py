def recursive_sort(sith_names):
    if len(sith_names) <= 1:
        return sith_names
    pivot = sith_names[0]
    left = [x for x in sith_names[1:] if x < pivot]
    right = [x for x in sith_names[1:] if x >= pivot]
    return recursive_sort(left) + [pivot] + recursive_sort(right)

sith_names = ['Darth Vader', 'Darth Maul', 'Darth Sidious']
sorted_names = recursive_sort(sith_names)