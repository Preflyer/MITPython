### Week 3
### Lecture 5

### Write an iterative function iterPower(base, exp) that calculates the 
vexponential baseexp by simply using successive multiplication

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    result = 1
    while exp > 0:
        result *= base
        exp -= 1
    return result


### Write a function recurPower(base, exp) which computes baseexp 
### by recursively calling itself to solve a smaller version of 
### the same problem, and then multiplying the result by base to 
### solve the initial problem

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if base == 1 or exp == 0:
        return 1
    return base*recurPower(base, exp-1)


### Write a procedure recurPowerNew which recursively computes 
### exponentials using this idea

def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float; base^exp
    '''
    if base == 1 or exp == 0:
        return 1
    elif exp % 2 != 0:
        return base*recurPowerNew(base,exp-1)
    return recurPowerNew(base*base, exp/2)
    

### Write an iterative function, gcdIter(a, b), that implements 
### this idea. One easy way to do this is to begin with a test 
### value equal to the smaller of the two input arguments, and 
### iteratively reduce this test value by 1 until you either reach 
### a case where the test divides both a and b without remainder, 
### or you reach 1

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a == 1 or b == 1:
        return 1    
    elif max(a,b) % min(a,b) == 0:
        return min(a,b)
    else:
        lo = min(a,b)
        while a % lo != 0 or b % lo != 0:
            lo -= 1
        return lo   


### Write a function gcdRecur(a, b) that implements this idea recursively. 
### This function takes in two positive integers and returns one integer.

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b == 0:
        return a
    return gcdRecur(b, a % b)


### Write an iterative function, lenIter, which computes the length of an input 
### argument (a string), by counting up the number of characters in the string.

def lenIter(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    length = 0
    for c in aStr:
        length += 1
    return length

### Write a recursive function, lenRecur, which computes the length of an input 
### argument (a string), by counting up the number of characters in the string.

def lenRecur(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    if aStr == '':
        return 0
    else:
        return 1 + lenRecur(aStr[1:])


def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr) == 0:
        return False
    if len(aStr) == 1:
        return aStr == char
    midNum = len(aStr)/2
    midChar = aStr[midNum]
    if char == midChar:
        return True
    elif char < midChar:
        return isIn(char, aStr[:midNum])
    else: 
        return isIn(char, aStr[midNum+1:])
        

def semordnilap(str1, str2):
    '''
    str1: a string
    str2: a string
    
    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    '''
    if len(str1) != len(str2):
        return False
    if len(str1) == 1:
        return str1 == str2  
    if str1[0] == str2[-1]:
        return semordnilap(str1[1::], str2[:-1:])
    else:
        return False


### Lecture 6

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    
    return aTup[::2]


applyToEach(testList, abs)
 
 
def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    total = 0
    for value in aDict.values():
        total += len(value)
    return total


def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    keyLength = 0
    result = None
    for key in aDict.keys():
        if len(aDict[key]) >= keyLength:
            result = key
            keyLength = len(aDict[key])
    return result










