NEW_TASK = 1


class Processor:

    def __init__(self, a):
        self.a = a
        self.array_of_tasks = []
        self.rest_time = 0

    def add_task(self):
        self.array_of_tasks.append(NEW_TASK)

    def update(self, delta):
        result = False
        if self.rest_time > 0:
            self.rest_time -= delta
            if self.rest_time <= 0:
                result = True
                if len(self.array_of_tasks) > 0:
                    self.rest_time = self.a
                    self.array_of_tasks.pop()
                else:
                    self.rest_time = -1
        else:
            if len(self.array_of_tasks) > 0:
                self.rest_time = self.a
                self.array_of_tasks.pop()
        return result
