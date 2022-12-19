import distribution as d

FREE = 0
IN_PROCESS = 1


class Teacher:

    def __init__(self, a, b, name):
        self.a = a
        self.b = b
        self.state = FREE
        self.name = name
        self.rest_time = 0
        self.amount_of_students = 0

    def cur_state(self):
        return self.state

    def start_process(self):
        self.state = IN_PROCESS
        self.rest_time = d.EvenDistribution(self.a, self.b).generate()

    def update(self, delta):
        result = False
        if self.state == IN_PROCESS:
            self.rest_time -= delta
            if self.rest_time <= 0:
                self.amount_of_students += 1
                if (self.name == "Gavrilova") and (self.amount_of_students % 5 == 0):
                    self.amount_of_students += 1
                    self.rest_time += 40
                else:
                    self.state = FREE
                result = True
        return result
