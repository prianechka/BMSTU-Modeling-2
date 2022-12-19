import numpy as np
import typing


def create_probs_matrix(matrix_of_intensity: np.array) -> np.array:
    numbers_of_state = matrix_of_intensity.shape[0]

    matrix_of_probs = np.zeros(shape=(numbers_of_state + 1, numbers_of_state + 1))

    for cur_state_row in range(numbers_of_state):
        for i in range(numbers_of_state):
            if i != cur_state_row:
                matrix_of_probs[cur_state_row][i] = matrix_of_intensity[i][cur_state_row]
        matrix_of_probs[cur_state_row][cur_state_row] = -sum(matrix_of_intensity[cur_state_row])

    for i in range(numbers_of_state + 1):
        matrix_of_probs[numbers_of_state][i] = 1

    return matrix_of_probs

def build_a_matrix(matrix_of_probs: np.array) -> np.array:
    numbers_of_state = matrix_of_probs.shape[0] - 1

    result = matrix_of_probs[:numbers_of_state, :numbers_of_state]
    result[0, :] = matrix_of_probs[numbers_of_state, :numbers_of_state]

    return result

def build_b_matrix(matrix_of_probs: np.array) -> np.array:
    numbers_of_state = matrix_of_probs.shape[0] - 1

    return matrix_of_probs[:, numbers_of_state][::-1][:numbers_of_state]

def solve_equation(matrix_of_probs: np.array) -> np.array:
    a = build_a_matrix(matrix_of_probs)
    b = build_b_matrix(matrix_of_probs)

    return np.linalg.solve(a, b)

def find_limited_probabilities(intensity_matrix: np.array) -> np.array:
    return solve_equation(create_probs_matrix(intensity_matrix))