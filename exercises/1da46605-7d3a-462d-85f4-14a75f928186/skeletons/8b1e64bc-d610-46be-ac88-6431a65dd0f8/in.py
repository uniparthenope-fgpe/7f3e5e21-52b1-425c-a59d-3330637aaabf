def total_distance(jumps):
    total = 0
    for jump in jumps:
        total += jump
    return total

jumps = [0, 500, 1000, 1500]
print(total_distance(jumps))