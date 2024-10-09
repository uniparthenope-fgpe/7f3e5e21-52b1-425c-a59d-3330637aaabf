class TimeTurner:
    def __init__(self, hours):
        self.hours = hours
        self.time_travels = []
    def go_back(self):
        self.time_travels.append(self.hours)
        return f'Went back {self.hours} hours!'
