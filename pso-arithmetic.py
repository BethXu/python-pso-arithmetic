from particle import Particle

MAX_GENERATIONS = 400
NUM_PARTICLES = 20

def main():
   
    gBest = 100000
    gBestIndex = 0
    
    
    swarm = [Particle(0,100,50) for i  in range(NUM_PARTICLES)]
    
    generations = 0
    converged = False
    while(generations < MAX_GENERATIONS and (converged == False)):
        
        for i in range(NUM_PARTICLES):
            swarm[i].calculateFitness()
            if (swarm[i].fitness == 0):
                converged = True
              
        print "[" + str(converged) + "] Generation: " + str(generations)
        for i in range(NUM_PARTICLES):
            print swarm[i]
            
        for i in range(NUM_PARTICLES):
            if (swarm[i].pBest < gBest):
                gBest = swarm[i].pBest
                gBestIndex = i
        
        for i in range(NUM_PARTICLES):
            if (i != gBestIndex):
                swarm[i].update(gBest)
                
        generations = generations + 1

if __name__ == '__main__':
    main()