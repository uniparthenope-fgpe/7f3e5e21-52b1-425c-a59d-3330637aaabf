class Event:
    def __init__(self, name, start, end):
        self.name = name
        self.start = start
        self.end = end

class Scheduler:
    def __init__(self):
        self.events = []

    def add_event(self, event):
        for e in self.events:
            if (event.start < e.end) and (event.end > e.start):
                return 'Overlap detected'
        self.events.append(event)
        return 'Event added'