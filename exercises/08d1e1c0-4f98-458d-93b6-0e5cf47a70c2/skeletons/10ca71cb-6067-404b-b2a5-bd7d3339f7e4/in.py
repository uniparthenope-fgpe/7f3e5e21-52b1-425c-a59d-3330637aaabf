class Scheduler:
    def __init__(self):
        self.classes = []

    def add_class(self, class_name):
        self.classes.append(class_name)

    def view_classes(self):
        return self.classes

# Example usage:
scheduler = Scheduler()
scheduler.add_class('Potions')