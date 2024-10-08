class Starship:
    def __init__(self, name):
        self.name = name
        self.crew = []
    
    def add_crew_member(self, member):
        self.crew.append(member)
    
    def remove_crew_member(self, member):
        self.crew.remove(member)
