import json


class Exporter:

    #def __init__(self):
    #    pass

    def save_tasks(self, tasks):
        self.f = json.dumps(tasks, indent=len(tasks))
 
        with open("taski.json", "w") as file:
            file.write(self.f)

        return
