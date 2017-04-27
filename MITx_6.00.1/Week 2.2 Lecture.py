### Week 2
### Lecture 3

def __str__(self):
        res = ''   # Change 1
        for b in self.buckets:
            for t in b:
                res = res + str(t[0]) + ':' + str(t[1]) + ','
        return '{' + res[:-1] + '}' # Change 2


### Lecture 4

def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if L == []:
        return float('NaN')
    values = []
    if L != []:
        for string in L:
            char = len(string)
            values.append(char)
        mean = sum(values)/float(len(values))
        total = 0.0
        for i in values:
            total += (i-mean)**2
        return (total/len(values))**0.5

    return (tot/len(X))**0.5





































