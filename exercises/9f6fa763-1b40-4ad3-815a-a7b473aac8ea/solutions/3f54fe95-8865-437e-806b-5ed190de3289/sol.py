class Transfiguration:
    def __init__(self, object):
        self.object = object
    def transform(self):
        if self.object == 'rat':
            return 'cup'
        elif self.object == 'teapot':
            return 'tortoise'
        else:
            return 'unknown'