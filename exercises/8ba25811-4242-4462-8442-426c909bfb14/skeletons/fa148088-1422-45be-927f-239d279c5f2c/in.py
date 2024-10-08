members = {}

def add_member(name, proficiency):
    members[name] = proficiency

# Save to file
with open('members.txt', 'w') as f:
    for name, proficiency in members.items():
        f.write(f'{name}: {proficiency}\n')