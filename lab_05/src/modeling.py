import distribution as d
import operators as o


def modeling(operators, processors, limit=300):
    amount_of_response = 0
    delta = 0.01
    time_to_generate_new_client = 0
    amount_of_refuses = 0
    amount_of_requests = 0

    while amount_of_requests < limit:
        i = 0
        for op in operators:
            result = op.update(delta)
            if result:
                if i < 2:
                    processors[0].add_task()
                else:
                    processors[1].add_task()
            i += 1

        if time_to_generate_new_client < 0:
            amount_of_requests += 1
            res = False
            for op in operators:
                if op.cur_state() == o.FREE:
                    op.start_process()
                    res = True
            time_to_generate_new_client = d.EvenDistribution(8, 12).generate()
            if not res:
                amount_of_refuses += 1
        time_to_generate_new_client -= delta
        for pr in processors:
            result = pr.update(delta)
            if result:
                amount_of_response += 1
    return amount_of_requests, amount_of_response, amount_of_refuses
