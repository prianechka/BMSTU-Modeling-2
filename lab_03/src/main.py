import numpy as np

np.random.seed(42)
def start_gen_sequence(a = 1, b = 999, seqsize = 1000):
    return np.random.choice(np.arange(a, b, 1), size=seqsize)


def single_table(sequence):
    np.random.shuffle(sequence)
    yield sequence


def generate_table_sequence(a = 1, b = 999, seqsize = 1000):
    X = start_gen_sequence(a, b, seqsize)
    np.random.shuffle(X)
    return X

def burton_critery(x, a, b, c, d):
    unique, counts = np.unique(x, return_counts=True)
    mean = np.mean(counts)
    numerator = 0
    denominator = 0
    n = counts.shape[0]
    for i in range(n - 1):
        numerator += np.power((counts[i] - counts[i + 1]), 2)
        denominator += np.power(counts[i] - mean, 2)
    denominator += np.power(counts[-1] + 1 - mean, 2)
    result = numerator / denominator
    ba = a + b*np.power(n, c)*np.power(np.log(n), d)
    return (result - (2 - ba)) * ((2 + ba) - result)


def func_generate(m, a, c, x0, seqsize=1000):
    X = []
    tmp = x0
    for i in range(seqsize):
        X.append(tmp)
        tmp = (tmp*a + c) % m
    return X


print(generate_table_sequence(1, 999, 25))

print(burton_critery([1, 2, 9, 3, 3, 5, 4, 8, 9, 1, 3, 8, 1, 5, 4, 9, 5, 1, 2, 3, 6, 9, 2, 3, 5],-0.023, 0.261, -0.345, 2.212))