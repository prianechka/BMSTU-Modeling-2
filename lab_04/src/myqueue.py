import request as r


class MyQueue:

    def __init__(self, limit):
        self.first_elem_index = 0
        self.last_elem_index = -1
        self.array = [r.Request(0)] * limit
        self.MaxLen = limit

    def enqueue(self, elem):
        if self.last_elem_index < (self.MaxLen - 1):
            self.last_elem_index += 1
            self.array[self.last_elem_index] = elem

    def is_empty(self):
        return self.last_elem_index < self.first_elem_index

    def dequeue(self):
        result = None
        if not self.is_empty():
            result = self.array[self.first_elem_index]
            self.first_elem_index += 1
        return result
