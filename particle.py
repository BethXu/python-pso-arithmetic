import random

class Particle:
    """
    Author: Stephen Sheridan
    Date: 04/03/2016
    Description: Simple particle class that contains attributes A, B, C, D
    in order to solve arithmetic problem A+B+C+D=50. The update method uses
    Eberhart & Kennedy's velocity update equation.
    """
    V_MAX = 10
    C1 = 2
    C2 = 2
    
    # Called when a new Particle object is instanciated
    def __init__(self, low, high, target):
        self.low = low
        self.high = high
        self.target = target
        # Set the class attribues A, B, C, D to random integer values between low and high    
        self.A = random.randint(low, high)
        self.B = random.randint(low, high)
        self.C = random.randint(low, high)
        self.D = random.randint(low, high)
        # Give PSO algorithm attributes some initial values
        self.pBest = abs((self.A+self.B+self.C+self.D) - self.target)
        self.velocity = 0
        self.fitness = self.pBest
            
    # Update the fitness value for this Particle and check to see if its better then current pBest
    def calculateFitness(self):
        # Calculate the distance from the TARGET value
        self.fitness = abs((self.A+self.B+self.C+self.D) - self.target)
        if (self.fitness < self.pBest):
            self.pBest = self.fitness

    # Update this particles attributes A, B, C, D based on Eberhart & Kennedy's equation
    def update(self, gBest):
        # Set test = to this particles current solution
        test = self.A+self.B+self.C+self.D
        # Generate some random numbers between 0 - 1 for equation
        R1 = random.random()
        R2 = random.random()

        # E B E R H A R T   &   K E N N E D Y
        self.velocity = self.velocity + Particle.C1 * R1 * (self.pBest - test) + Particle.C2 * R2 * (gBest - test)

        # Control the velocity, best to not let it go too wild
        if (self.velocity > Particle.V_MAX):
            self.velocity = Particle.V_MAX
        elif (self.velocity < -Particle.V_MAX):
            self.velocity = -Particle.V_MAX
        
        # Update attributes A, B, C, D with new velocity
        self.A = int(self.A + self.velocity)
        self.B = int(self.B + self.velocity)
        self.C = int(self.C + self.velocity)
        self.D = int(self.D + self.velocity)
    
    # Define how this Particle class will print out
    def __str__(self):
        total = self.A+self.B+self.C+self.D
        return "{0} + {1} + {2} + {3} = {4}".format(self.A, self.B, self.C, self.D, total)
        
        
        

    
    