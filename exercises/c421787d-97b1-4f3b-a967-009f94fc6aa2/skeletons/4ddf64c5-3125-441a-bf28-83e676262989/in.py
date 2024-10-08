def count_droids(droids):
    count = 0
    for droid in droids:
        if droid:
            count += 1
    return count

inventory = ['R2-D2', 'C-3PO', None, 'BB-8']
print(count_droids(inventory))