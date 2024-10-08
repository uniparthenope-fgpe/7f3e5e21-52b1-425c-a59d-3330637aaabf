from datetime import datetime

class Scheduler:
    def __init__(self):
        self.schedule = []

    def add_event(self, event_name, event_time):
        self.schedule.append({'name': event_name, 'time': event_time})

    def remove_event(self, event_name):
        self.schedule = [event for event in self.schedule if event['name'] != event_name]

    def view_schedule(self):
        return sorted(self.schedule, key=lambda x: x['time'])