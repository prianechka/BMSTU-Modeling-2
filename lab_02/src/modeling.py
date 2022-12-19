import numpy as np
import solve as s

EPS = 0.001
TIME_DELTA = 0.001

def modeling(intensity_matrix: np.array) -> np.array:
    number_of_states = intensity_matrix.shape[0]

    time = np.zeros(shape=(number_of_states))
    all_probs = [[] for _ in range(number_of_states)]
    all_times = []
    cur_probs = np.zeros(shape=(number_of_states))
    is_finished = [False for _ in range(number_of_states)]

    for i in range(number_of_states):
        cur_probs[i] = 1 / number_of_states

    real_probabilities = s.find_limited_probabilities(intensity_matrix)

    system_time = 0
    for _ in range(3000):
        delta = np.zeros(shape=(number_of_states))

        for cur_state_row in range(number_of_states):
            for i in range(number_of_states):
                if i != cur_state_row:
                    delta[cur_state_row] += intensity_matrix[i][cur_state_row] * cur_probs[i]
            delta[cur_state_row] -= cur_probs[cur_state_row] * sum(intensity_matrix[cur_state_row, :])
        cur_probs += delta * TIME_DELTA

        all_times.append(system_time)
        system_time += TIME_DELTA

        for i in range(number_of_states):
            all_probs[i].append(cur_probs[i])
            if np.abs(real_probabilities[i] - cur_probs[i]) <= EPS:
                if is_finished[i] == False:
                    time[i] = system_time
                    is_finished[i] = True

        if sum(is_finished) == number_of_states:
            break
    return real_probabilities, time, all_times, all_probs




