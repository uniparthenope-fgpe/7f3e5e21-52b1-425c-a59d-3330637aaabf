def droid_factory(n):
    count = 0
    for i in range(n):
        if i % 2 == 0:
            count += 1
    return count

print(droid_factory(10))  # Should return 5