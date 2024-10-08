import json

events = []

def add_event(event):
    events.append(event)


def save_events(filename):
    with open(filename, 'w') as file:
        json.dump(events, file)


def load_events(filename):
    global events
    with open(filename, 'r') as file:
        events = json.load(file)