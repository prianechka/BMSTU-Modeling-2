import numpy as np
import modeling as m
import graph as g

matrix_of_intensity = np.array(
    [[0, 0.5, 0, 0, 0],
     [0, 0, 2, 0, 0],
     [0, 0, 0.2, 1.3, 1.5],
     [0.8, 0, 0, 0, 0],
     [2, 0, 0, 0, 0]])

real_probs, fact_time, all_times, all_probs = m.modeling(matrix_of_intensity)
#print(real_probs)
# g.graph(matrix_of_intensity)
print(real_probs)
print(fact_time)
#print(all_probs)
g.graph_probability_over_time(real_probs, fact_time, all_times, all_probs)