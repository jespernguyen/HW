# used in the last part of the homework assignment
import turtle
import math

def fizzBuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'fizzBuzz'
    if n % 3 == 0:
        return 'fizz'
    elif n % 5 == 0:
        return 'Buzz'
    else:
        return str(n)

def age(date, month, year):
    ageyear = 2025 - year
    if month < 10:
        return ageyear
    elif  date < 16 and month <= 10:
        return ageyear
    else:
        return ageyear - 1
    
def countPos(l):
    if l == []:
        return 0
    else:
        counter = 1
        head = l[0]
        tail = l[1:]
        tailResult = countPos(tail)
        if head > 0:
            return counter + tailResult
        else:
            return tailResult
        
def threshold(l, n):
    if l == []:
        return []
    else:
        head = l[0]
        tail = l[1:]
        tailResult = threshold(tail, n)
        if n >= head:
            return [n] + tailResult
        else:
            return [head] + tailResult #original head keeps the numbers that are greater than n


def intRange(low, high):
    if low >= high:
        return []
    else:
        return [low] + intRange(low + 1, high)
    
def innerLists(l):
    if l == []:
        return []
    else:
        head = l[0]
        tail = l[1:]
        tailResult = innerLists(tail)
        return [intRange(1, head + 1)] + tailResult
        

#Problem set 2: Recursive Art

def NGonHelper(n, sideLength, angle):
    if n == 0:
        return
    else:
        turtle.forward(sideLength)
        turtle.left(angle)
        NGonHelper(n-1, sideLength, angle)
    return  
       
def regularNGon(n, sideLength):
    angle = 360//n
    return NGonHelper(n, sideLength, angle)
 


def archSpiral(length, increment, angle, n):
    if n == 0:
        return
    else:
        spiralLength = length + increment
        turtle.forward(length) # FUCKING INTIAL LENGTH JESUS FUCKING CHRIST
        turtle.left(angle)
        archSpiral(spiralLength, increment, angle, n-1)
        return

def logSpiral(length, percentIncrease, angle, n):
    if n == 0:
        return
    else:
        percent = 1 + (percentIncrease/100)
        spiralLength = length * percent
        turtle.forward(length)
        turtle.left(angle)
        logSpiral(spiralLength, percentIncrease, angle, n-1)
        return



# get the even numbers from a list
# evens([4, 22, 1, 11, 5, 6, 7]) returns [1, 11, 5, 7]

# produce only the long strings from a list of strings
# longStrings(['hi', 'there', 'class']) returns ['there', 'class']

# Python's filter function encodes this pattern of walking over a list
# and keeping only a subset of the items
# filter takes two arguments:
# - the second argument is the list to traverse
# - the first argument is a function that takes an item of the list and
#		return True or False

def isOdd(n):
    if n  % 2 == 1:
        return True
    else:
        return False

def isLongString(s):
    if len(s) >= 4:
        return True
    else:
        return False

def longStrings(l):
    return list(filter(isLongString, l))

    
def alwaysTrue(x):
    return True
def alwaysFalse(x):
    return False

#task: given a list of lists, remove all of the inner empty lists
# removeEmpty([1, 2, 3], [], [4], [5,6], [], [789]] returns

def emptylist(s):
    if s == []:
        return False
    else:
        return True
        
def removeEmpty(l):
    return list(filter(emptylist, l))

