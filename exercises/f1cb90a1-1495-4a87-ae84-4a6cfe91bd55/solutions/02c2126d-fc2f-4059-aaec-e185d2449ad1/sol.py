droids = []
def add_droid(name):
    droids.append(name)

add_droid('R2-D2')
add_droid('BB-8')

for droid in droids:
    print(f'Droid Name: {droid}')