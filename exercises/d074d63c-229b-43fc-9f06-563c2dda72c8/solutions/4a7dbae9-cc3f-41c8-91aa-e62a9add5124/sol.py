from datetime import datetime

class Scheduler:
    def __init__(self):
        self.schedule = []

    def add_event(self, event, time):
        self.schedule.append({'event': event, 'time': time})

    def view_schedule(self):
        return self.schedule

scheduler = Scheduler()
scheduler.add_event('Potions Class', '10:00 AM')
scheduler.add_event('Quidditch Practice', '2:00 PM')
print(scheduler.view_schedule())