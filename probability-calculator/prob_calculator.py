import copy
import random
from collections import Counter
# Consider using the modules imported above.

class Hat:

    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)

    def draw(self, n):
        if n >= len(self.contents):
            drawn_balls = self.contents.copy()
            self.contents.clear()
            return drawn_balls
        else:
            drawn_balls = random.sample(self.contents, n)
            for ball in drawn_balls:
                self.contents.remove(ball)
            return drawn_balls

def is_subdict(small, big):
    return dict(big, **small) == big

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0
    exp_balls = []
    for color, count in expected_balls.items():
        exp_balls.extend([color] * count)

    for i in range(num_experiments):
        copy_hat = copy.deepcopy(hat)
        drawn_balls = copy_hat.draw(num_balls_drawn)
        if all(drawn_balls.count(ball) >= exp_balls.count(ball) for ball in exp_balls):
            m += 1
    return m / num_experiments




hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)

print(probability)
