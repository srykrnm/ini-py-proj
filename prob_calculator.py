import random
import copy

### FUNCTIONS AND CLASSES ###

class Hat:
    def __init__(self, **kwargs):
        self.drawn_balls = []
        self.contents = []
        for k, v in kwargs.items():
            for i in range(v):
                self.contents.append(k)
    def draw(self, no_items):
        for _ in range(no_items):
            if no_items >= len(self.contents):
                self.drawn_balls = self.contents
                self.contents = []
            else:
                self.del_index = random.randint(0, (len(self.contents) - 1))
                self.drawn_balls.append(self.contents.pop(self.del_index))
        return self.drawn_balls

def experiment(hat_object, expected_balls:int , num_balls_drawn: int, num_experiments: int):
    successful_experiments = 0
    for _ in range(num_experiments):
        hat_object_copy = copy.deepcopy(hat_object) 
        drawn_balls = hat_object_copy.draw(num_balls_drawn)
        match = True
        for ball, count in expected_balls.items():
            if drawn_balls.count(ball) < count:
                match = False
                break
        if match:
            successful_experiments += 1
    probability = successful_experiments / num_experiments
    return probability

### MAIN ###

hat = Hat(red=50)
expected_balls = {"red": 1}
num_balls_drawn = 4
num_experiments = 1000
probability = experiment(hat, expected_balls, num_balls_drawn, num_experiments)
print("The probability is:", probability)

### END ###