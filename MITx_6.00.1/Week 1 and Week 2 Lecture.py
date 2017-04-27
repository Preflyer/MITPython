### Week 1

### Print 'hello world'
print('hello world')



### Print 'hello world' if the value of happy is greater than 2 
if happy > 2:
    print('hello world')



### Write a piece of Python code that prints out one of the following messages:
###"string involved" if either varA or varB are strings
###"bigger" if varA is larger than varB
###"equal" if varA is equal to varB
###"smaller" if varA is smaller than varB

if type(varA) == str or type(varB) == str:
    print('string involved')
elif varA == varB:
    print('equal')
elif varA > varB:
    print('bigger')
else:
    print('smaller')




### Week 2


### 1. Convert the following into code that uses a while loop.
### print 2
### print 4
### print 6
### print 8
### print 10
### print Goodbye!

num = 0
while num < 10:
    num += 2
    print(num)
print('Goodbye!')


### 1. Convert the following code into code that uses a for loop.
### print 2
### print 4
### print 6
### print 8
### print 10
### print "Goodbye!"

num = 0
for num in range(2,12,2):
    print num
print('Goodbye!')


### 2. Convert the following code into code that uses a for loop.
### print "Hello!"
### print 10
### print 8
### print 6
### print 4
### print 2

print('Hello!')
num = 0
for num in range(10,0, -2):
    print num


### Create a program that guesses a secret number
### Enter 'h' to indicate the guess is too high
### Enter 'h' to indicate the guess is too high
### Enter 'c' to indicate I guessed correctly

low = 0
high = 100
mid = (high+low)/2
print("Please think of a number between 0 and 100!")
while True:
    print("Is your secret number " + str(mid) + "?")
    guess = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too high. Enter 'c' to indicate I guessed correctly. ")
    if guess == 'l':
        low = mid
        mid = (low + high)/2       
    elif guess == 'h':
        high = mid
        mid = (high + low)/2
    elif guess == 'c':
        break
    else:
        print("Sorry, I did not understand your input.")
        
print("Game over. Your secret number was: " + str(mid))


### Write a Python function, square, that takes in one number
### and returns the square of that number

def square(x):
    '''
    x: int or float.
    '''
    x = x**2
    return x
    

def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    y = a*x**2 + b*x + c
    return y


def clip(lo, x, hi):
    '''
    Takes in three numbers and returns a value based on the value of x.
    Returns:
     - lo, when x < lo
     - hi, when x > hi
     - x, otherwise
    '''
    return min(max(x,lo),hi)
    
    
def fourthPower(x):
    '''
    x: int or float.
    '''
    return square(square(x))


def odd(x):
    '''
    x: int or float.

    returns: True if x is odd, False otherwise
    '''
    return (x%2 == 1)


def isVowel(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    # Your code here
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        return True
    elif char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U':
        return True
    else:
        return False


def isVowel2(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    # Your code here
    if char in 'aeiouAEIOU':
        return True
    else:
        return False








