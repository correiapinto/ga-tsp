import random

class LoadPoints:
    def __init__(self):
        self.n_points = 10

    def create_random_points(self):
        x = list()
        y = list()
        for i in range(self.n_points):
            x.append(random.randint(-20, 20))
            y.append(random.randint(-20, 20))
        return x, y

