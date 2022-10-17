import random

class Hat:
    def __init__(self, **ballnumber):
        self.balls = ballnumber
        self.contents=[]
        for i,j in ballnumber.items():
            for k in range(j):
                self.contents.append(i)
    
    def draw(self, take: int):
        self.drawn= []
        m = self.contents[:]
        if take < len(m):
            for i in range(take):
                selection = random.choice(m)
                self.drawn.append(selection)
                m.remove(selection)
        else:
            self.drawn = m[:]

        return self.drawn


def experiment(hat: Hat, expected_balls: dict, 
                num_balls_drawn:int, num_experiments):
    M = 0
    N = num_experiments

    for i in range(N):
        hat.draw(num_balls_drawn)
        sampled = hat.drawn
        is_satisfied = True
        for key,value in expected_balls.items():
            if sampled.count(key) < value:
                is_satisfied = False
                break
        
        if is_satisfied:
            M+=1
        
    prob = M/N
    print(prob)
    
                   

hat1 = Hat(blue= 3, red = 2, green = 6)
probability = experiment(hat1, {'blue':2, 'green':1}, 4,20000)

