def add_droid(inventory, droid):
    inventory.append(droid)
    return inventory

inventory = ['R2-D2', 'C-3PO']
new_droid = 'BB-8'

# Call the function to add the new droid
updated_inventory = add_droid(inventory, new_droid)
print(updated_inventory)