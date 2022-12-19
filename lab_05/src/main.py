import modeling as m
import operators as o
import processors as p

operators = [
    o.Operator(15, 25),
    o.Operator(30, 50),
    o.Operator(20, 60)
]

processors = [
    p.Processor(15),
    p.Processor(30)
]

result = m.modeling(operators, processors, 100)
print(result)
