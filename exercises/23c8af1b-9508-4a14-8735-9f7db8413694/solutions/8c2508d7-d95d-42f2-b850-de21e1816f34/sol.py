class Jedi:
    def __init__(self, name, power_level):
        self.name = name
        self.power_level = power_level

class JediEvaluator:
    def __init__(self):
        self.jedi_list = []

    def add_jedi(self, jedi):
        self.jedi_list.append(jedi)

    def evaluate(self):
        return sorted(self.jedi_list, key=lambda x: x.power_level, reverse=True)