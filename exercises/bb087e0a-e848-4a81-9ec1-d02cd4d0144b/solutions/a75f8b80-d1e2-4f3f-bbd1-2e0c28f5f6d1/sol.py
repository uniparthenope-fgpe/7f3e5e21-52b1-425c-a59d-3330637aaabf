droid_inventory = {}
def add_droid(name, model):
    droid_inventory[name] = model

def remove_droid(name):
    if name in droid_inventory:
        del droid_inventory[name]

def list_droids():
    for name, model in droid_inventory.items():
        print(f'Droid: {name}, Model: {model}')