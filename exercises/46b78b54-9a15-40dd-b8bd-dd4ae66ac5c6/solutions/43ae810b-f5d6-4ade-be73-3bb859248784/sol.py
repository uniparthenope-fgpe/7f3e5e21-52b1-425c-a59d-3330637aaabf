def save_creature(creature):
    with open('creatures.txt', 'a') as f:
        f.write(creature + '\n')

def retrieve_creatures():
    with open('creatures.txt', 'r') as f:
        return f.readlines()

save_creature('Unicorn')
print(retrieve_creatures())