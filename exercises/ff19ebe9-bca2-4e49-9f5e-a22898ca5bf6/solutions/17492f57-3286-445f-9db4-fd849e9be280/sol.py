def produce_droids(droid_names):
    produced_droids = []
    for name in droid_names:
        produced_droids.append(name + ' Droid')
    return produced_droids

droid_list = ['R2-D2', 'C-3PO', 'BB-8']
print(produce_droids(droid_list))