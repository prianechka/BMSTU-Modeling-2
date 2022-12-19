import modeling as m
import operators as o
import processors as p

teachers = [
    o.Teacher(10, 30, "Stroganov"),
    o.Teacher(17, 33, "Gavrilova"),
    o.Teacher(5, 60, "Kostriski")
]

masters = [
    p.Master(10),
    p.Master(15)
]

result = m.modeling(teachers, masters, 200)
print(result, (result[0] - result[1]) / result[0])
