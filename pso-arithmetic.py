from particle import Particle

# Define some globals to control swarm
MAX_GENERATIONS = 400
NUM_PARTICLES = 20

def main():
    # Keep track of global best solution and its index within the swarm   
    gBest = 100000
    gBestIndex = 0
    
    # Make the swarm - create a list of Particles of size NUM_PARTICLES
    swarm = [Particle(0,100,50) for i  in range(NUM_PARTICLES)]
    
    # Set the loop counter and stopping condition
    generations = 0
    converged = False
    while(generations < MAX_GENERATIONS and (not converged)):
        
        # Calculate the fitness values for the swarm and check if we have a solution
        for i in range(NUM_PARTICLES):
            swarm[i].calculateFitness()
            converged = converged or (swarm[i].fitness == 0)
              
        # Print some output at this point 
        print "[] Generation: " + str(generations)
        for i in range(NUM_PARTICLES):
            print swarm[i]
        
        # Set the global best based on the swarm at this point    
        for i in range(NUM_PARTICLES):
            if (swarm[i].pBest < gBest):
                gBest = swarm[i].pBest
                gBestIndex = i
        
        # Update all but the global best particle using Eberhart & Kennedy's equation        
        for i in range(NUM_PARTICLES):
            if (i != gBestIndex):
                swarm[i].update(gBest)
        
        # Set the next time step        
        generations = generations + 1

if __name__ == '__main__':
    main()