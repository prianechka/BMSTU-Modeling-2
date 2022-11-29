import random

import distributions as d
import models as m

a, b = 1, 5
request_generator = d.EvenDistribution(a, b)
k, alpha = 1, 1
oa_generator = d.ErlangDistribution(k, alpha)
event_model = m.EventModel(request_generator, oa_generator)
print(event_model.event())
delta = 0.001
time_model = m.TimeModel(request_generator, oa_generator, delta)
print(time_model.event())
