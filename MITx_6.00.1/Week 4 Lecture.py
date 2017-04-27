###  Week 4
### Lecture 7

def integerDivision(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the integer division of x divided by a.
    """
    count = 0
    while x >= a:
        count += 1
        x = x - a
    return count


### Lecture 8

#define the SimpleDivide function here:
def SimpleDivide(item, denom):
    try:
        return item / denom
    except ZeroDivisionError:
        return 0


































