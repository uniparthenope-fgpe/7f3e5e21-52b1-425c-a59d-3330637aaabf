droids = ['R2-D2', 'C-3PO', 'BB-8']
for droid in droids:
    print('Droid: ' + droid)
    # Fix the bug below
    if droid == 'R2-D2':
        print('Astromech Droid!')
    elif droid == 'C-3PO':
        print('Protocol Droid!')
    else:
        print('Unknown Droid!')