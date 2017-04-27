def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    assert x > 0, 'x is not positive'
    assert b >=2, 'b is not >= 2' 
    logger = 0 
    while b**logger <= x:
        logger += 1
    return logger-1


def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    newString = ''
    if len(s1) == 0:
        newString = s2[:]
        return newString
    elif len(s2) == 0:
        newString = s1[:]
        return newString
    else:
        if len(s1) > len(s2):
            (s1, remainder) = (s1[0:len(s2)], s1[len(s2):])
        elif len(s2) > len(s1): 
            (s2, remainder) = (s2[0:len(s1)], s2[len(s1):])
        else:
            remainder = ''
        firstString = []
        for i in range(len(s1)):
            firstString.append(s1[i])
            firstString.append(s2[i])
        newString = "".join(firstString) + remainder
        return newString


def laceStringsRecur(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    def helpLaceStrings(s1, s2, out):
        if s1 == '':
            return out + s2
        if s2 == '':
            return out + s1
        else:
            return helpLaceStrings(s2, s1[1:], out +s1[0])
    return helpLaceStrings(s1, s2, '')


def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    if n < 6:
        return False
    elif n == 6 or n == 9 or n == 20 or n > 34:
        return True
    elif n%6 == 0 or n%9 == 0 or n%20 == 0:
        return True
    else:
        while n >= 20:
            return McNuggets(n-20)
        while n >= 9:
            return McNuggets(n-9)
        while n >= 6:
            return McNuggets(n-6)
    

def fixedPoint(f, epsilon):
    """
    f: a function of one argument that returns a float
    epsilon: a small float
  
    returns the best guess when that guess is less than epsilon 
    away from f(guess) or after 100 trials, whichever comes first.
    """
    guess = 1.0
    for i in range(100):
        if abs(f(guess) - guess) < epsilon:
            return guess
        else:
            guess = f(guess) 
    return guess


def sqrt(a):
    def tryit(x):
        return 0.5 * (a/x + x)
    return fixedPoint(tryit, 0.0001)


def babylon(a):
    def test(x):
        return 0.5 * ((a / x) + x)
    return test

def sqrt(a):
    return fixedPoint(babylon(a), 0.0001)































