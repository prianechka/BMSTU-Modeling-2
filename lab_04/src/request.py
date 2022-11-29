class Request:

    def __init__(self, req_id):
        self.id = req_id
        self.waiting_time = 0
        self.all_time = 0
        self.attempts = 0
        