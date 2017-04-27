def drawing_without_replacement_sim(numTrials):
    """
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    """
    tally = 0
    for i in range(numTrials):
        bucket = [1,1,1,1,0,0,0,0]
        draw = []
        for i in range(3):
            j = random.choice(bucket)
            draw.append(j)
            bucket.remove(j)
        if draw == [0,0,0] or draw == [1,1,1]:
            tally += 1
    return tally/float(numTrials)



def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    numBins = float(numBins)

    pylab.hist(values,numBins)
    pylab.ylabel(yLabel)
    pylab.xlabel(xLabel)
    if title == None:
        pass
    else:
        pylab.title(title)
    pylab.show()
    
    
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls.
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    maxRuns = []
    for i in range(numTrials):
        dieRolls = []
        for i in range(numRolls):
            dieRolls.append(die.roll())
        maxRun = 1
        run = 1
        for i in range(len(dieRolls)-1):
            if dieRolls[i] == dieRolls[i+1]:
                run += 1
                if run > maxRun:
                    maxRun = run
                continue
            if dieRolls[i] != dieRolls[i+1]:
                run = 1
                continue
        maxRuns.append(maxRun)
        #print maxRuns
    makeHistogram(maxRuns,10, 'Max Run', '# of Runs','get-sum')
        
    return (sum(maxRuns) / float(len(maxRuns)))
    
    
    
    
    
       
























































