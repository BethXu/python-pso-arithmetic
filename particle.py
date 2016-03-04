import random

class Particle:
    """This is a simple particle class"""
    V_MAX = 10
    C1 = 2
    C2 = 2
    def __init__(self, low, high, target):
        self.low = low
        self.high = high
        self.target = target
        
        self.A = random.randint(low, high)
        self.B = random.randint(low, high)
        self.C = random.randint(low, high)
        self.D = random.randint(low, high)
        
        self.pBest = abs((self.A+self.B+self.C+self.D) - self.target)
        self.velocity = 0
        self.fitness = self.pBest
            
    def calculateFitness(self):
        self.fitness = abs((self.A+self.B+self.C+self.D) - self.target)
        if (self.fitness < self.pBest):
            self.pBest = self.fitness

    def update(self, gBest):
        test = self.A+self.B+self.C+self.D
        r1 = random.random()
        r2 = random.random()
        self.velocity = self.velocity + Particle.C1 * r1 * (self.pBest - test) + Particle.C2 * r1 * (gBest - test)
        if (self.velocity > Particle.V_MAX):
            self.velocity = Particle.V_MAX
        elif (self.velocity < -Particle.V_MAX):
            self.velocity = -Particle.V_MAX
        
        self.A = int(self.A + self.velocity)
        self.B = int(self.B + self.velocity)
        self.C = int(self.C + self.velocity)
        self.D = int(self.D + self.velocity)
    
    def __str__(self):
        total = self.A+self.B+self.C+self.D
        return "{0} + {1} + {2} + {3} = {4} Fitness = {5}".format(self.A, self.B, self.C, self.D, total, self.fitness)
        
        
        

    
    