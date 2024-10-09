def count_creatures(creatures):
    count = 0
    for creature in creatures:
        if creature == 'Unicorn':
            count += 1
    return count
# Test the function with a list of creatures