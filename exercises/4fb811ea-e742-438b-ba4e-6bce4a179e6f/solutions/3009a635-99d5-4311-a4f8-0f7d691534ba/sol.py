class Event:
    def __init__(self, title, time):
        self.title = title
        self.time = time

class Scheduler:
    def __init__(self):
        self.events = []
    
    def add_event(self, event):
        self.events.append(event)
    
    def show_schedule(self):
        for event in self.events:
            print(f'{event.title} at {event.time}')