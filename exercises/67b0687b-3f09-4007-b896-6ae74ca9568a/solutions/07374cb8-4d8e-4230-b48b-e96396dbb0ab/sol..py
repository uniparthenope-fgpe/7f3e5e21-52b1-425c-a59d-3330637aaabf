class Character:
    def __init__(self, name):
        self.name = name

    def time_travel(self, event):
        # Logic to revisit past events
        return f'{self.name} revisits {event}'

harry = Character('Harry')
event = 'Battle of Hogwarts'
print(harry.time_travel(event))