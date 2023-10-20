import json


class Importer:
    data = []

    #def __init__(self):
    #    pass

    def read_tasks(self):
        self.f = open('taski.json')
        self.data = json.load(self.f)
        self.f.close()
        return

    def get_tasks(self):
        return self.data