
import functools

# Write your functions here!

def TriHelper(l):
        if pow(l[0], 2) + pow(l[1], 2) == pow(l[2], 2):
            return True
        else:
            return False
    
def rightTriangles(l):
    return list(filter(lambda x: pow(x[0], 2) + pow(x[1], 2) == pow(x[2], 2), l))


def threshold(l, n):
    return list(map(lambda x: n if  x < n else x, l))


def countHelper(f, l):
    return list(filter(f, l))


def countOccurrences(f, l):
    return len(countHelper(f, l))
  
def toUpper(s):
    if 97 <= ord(s) <= 122:
        return chr(ord(s) - 32)
    else:
        return s
    
def toLower(s):
    if 65 <= ord(s) <= 90:
        return chr(ord(s) + 32)
    else:
        return s

def allLower(s):
    if s == '':
        return ''
    else:
        return functools.reduce(lambda x, y: x + y,list(map(toLower, s)), '')

def capitalize(s):
    return toUpper(s[0]) + allLower(s[1:])
    

def titleHelper(s):
    if len(s) >= 4:
        return capitalize(s)
    else:
        return allLower(s)
    

def title(l):
    firstword = l[0]
    processedFirst = capitalize(firstword)
    return [processedFirst] + list(map(titleHelper, l[1:]))

#remove all 0s from inner lists
# l is a list of integers lists
# removeAllZeros([1,2],[0,5,6,0], [3,0]) returns [[1,2], [5,6], [3]]
def removeAllZeros(l0):
    removeAll = lambda innerList: list(filter(lambda x: x!= 0, innerList))
    return list(map(returnZeros, l))


#mer
