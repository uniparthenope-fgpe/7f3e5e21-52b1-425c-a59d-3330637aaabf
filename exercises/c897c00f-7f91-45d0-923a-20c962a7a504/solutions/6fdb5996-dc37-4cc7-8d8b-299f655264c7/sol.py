droids = []
def add_droid(droid):
    droids.append(droid)

def remove_droid(droid):
    droids.remove(droid) if droid in droids else print('Droid not found')