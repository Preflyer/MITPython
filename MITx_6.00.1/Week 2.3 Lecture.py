### Week 3
### Lecture 5


def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    total = 0
    for i in range(numTrials):
        bowl = [1,1,1,0,0,0]
        pulled = []
        for i in range(3):
            a = random.choice(bowl)
            pulled.append(a)
            bowl.remove(a)
        if pulled == [1,1,1] or pulled == [0,0,0]:
            total += 1
    return total/float(numTrials) 


### Lecture 6

Refer to notes



































