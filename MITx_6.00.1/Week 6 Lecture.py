### Week 6
### LEcture 11

class Clock(object):
    def __init__(self, time):
	self.time = time
    def print_time(self):
	time = '6:30'
	print self.time

clock = Clock('5:30')
clock.print_time()


class Clock(object):
    def __init__(self, time):
	self.time = time
    def print_time(self, time):
	print time

clock = Clock('5:30')
clock.print_time('10:30')


class Clock(object):
    def __init__(self, time):
	self.time = time
    def print_time(self):
	print self.time

boston_clock = Clock('5:30')
paris_clock = boston_clock
paris_clock.time = '10:30'
boston_clock.print_time()



class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
    def __eq__(self,other):
        assert type(other) == type(self)
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        return 'Coordinate(' + str(self.x) + ', ' + str(self.y) + ')'


class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
        
    def intersect(self,other):
        """Returns a new intSet composed of integers that exist in both
        self and other"""
        intersectSet = intSet()
        for val in self.vals:
            if other.member(val):
                intersectSet.insert(val)
        return intersectSet
    
    def __len__(self):
        """Returns the number of elements in s"""
        return (len(self.vals))
        
        
class Queue(object):
    """creates a queue with FIFO removal"""
    def __init__(self):
        self.vals = []
    def insert(self,e):
        self.vals.append(e)
    def remove(self):
        try:
            return self.vals.pop(0)
        except:
            raise ValueError()       
    def __str__(self):
        self.vals.sort()
        return ('{' + ','.join([str(e) for e in self.vals]) + '}')
        
    
            
Lecture #12       
        
class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')
    def getDescription(self):
        return 'This charm summons an object to the caster, potentially over a significant distance.'



import random 

class Hand(object):
    def __init__(self, n):
        '''
        Initialize a Hand.

        n: integer, the size of the hand.
        '''
        assert type(n) == int
        self.HAND_SIZE = n
        self.VOWELS = 'aeiou'
        self.CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

        # Deal a new hand
        self.dealNewHand()

    def dealNewHand(self):
        '''
        Deals a new hand, and sets the hand attribute to the new hand.
        '''
        # Set self.hand to a new, empty dictionary
        self.hand = {}

        # Build the hand
        numVowels = self.HAND_SIZE / 3
    
        for i in range(numVowels):
            x = self.VOWELS[random.randrange(0,len(self.VOWELS))]
            self.hand[x] = self.hand.get(x, 0) + 1
        
        for i in range(numVowels, self.HAND_SIZE):    
            x = self.CONSONANTS[random.randrange(0,len(self.CONSONANTS))]
            self.hand[x] = self.hand.get(x, 0) + 1
            
    def setDummyHand(self, handString):
        '''
        Allows you to set a dummy hand. Useful for testing your implementation.

        handString: A string of letters you wish to be in the hand. Length of this
        string must be equal to self.HAND_SIZE.

        This method converts sets the hand attribute to a dictionary
        containing the letters of handString.
        '''
        assert len(handString) == self.HAND_SIZE, "Length of handString ({0}) must equal length of HAND_SIZE ({1})".format(len(handString), self.HAND_SIZE)
        self.hand = {}
        for char in handString:
            self.hand[char] = self.hand.get(char, 0) + 1


    def calculateLen(self):
        '''
        Calculate the length of the hand.
        '''
        ans = 0
        for k in self.hand:
            ans += self.hand[k]
        return ans
    
    def __str__(self):
        '''
        Display a string representation of the hand.
        '''
        output = ''
        hand_keys = self.hand.keys()
        hand_keys.sort()
        for letter in hand_keys:
            for j in range(self.hand[letter]):
                output += letter
        return output

    def update(self, word):
        """
        Does not assume that self.hand has all the letters in word.

        Updates the hand: if self.hand does have all the letters to make
        the word, modifies self.hand by using up the letters in the given word.

        Returns True if the word was able to be made with the letter in
        the hand; False otherwise.
        
        word: string
        returns: Boolean (if the word was or was not made)
        """
        newHand = self.hand.copy()
        for char in word:
            try:
                newHand[char] -= 1
            except:
                return False
        for char in newHand.keys():
            if newHand[char] < 0:
                return False
        self.hand = newHand
        return True            

myHand = Hand(7)
print myHand
print myHand.calculateLen()

myHand.setDummyHand('aazzmsp')
print myHand
print myHand.calculateLen()

myHand.update('za')
print myHand




def genPrimes():
    x = 1
    p = []
    while True:
        x += 1
        for char in p:
            if (x % char) == 0:
                break
        else:
            p.append(x)
            yield x
        
 