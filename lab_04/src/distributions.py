import random
import scipy.stats as ss


class EvenDistribution:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def generate(self):
        return self.a + (self.b - self.a) * random.random()


class ErlangDistribution:
    def __init__(self, k, alpha):
        self.k = k
        self.alpha = alpha

    def generate(self):
        return ss.erlang.rvs(self.k, self.alpha)
    