def count_bugbears(bugbears):
    count = 0
    for bugbear in bugbears:
        if bugbear == 'Bugbear':
            count += 1
    return count

print(count_bugbears(['Bugbear', 'Goblin', 'Bugbear']))