
# a few problems will use functions from this library
import math

def totalSeconds(s1, s2, s3):
    sec = s1
    minutes = s2 * 60
    hr = s3 * 3600
    return sec + minutes + hr


# write the function money
def moneyTEST():
    assert money(100, 7, 2) == 114.49
    
def money(m1, m2, m3):
    P = m1
    r = m2
    t = m3
    return  round(P * pow((1 + r * .01), t), 2)
    

# write the function distanceFromNearestSquare
def distanceFromNearestSquareTEST():
     assert distanceFromNearestSquare(13) == 3

def distanceFromNearestSquare(d):
    checkroot = math.isqrt(d)
    isqrsqr = pow(checkroot, 2)
    lower = math.isqrt(d) - 1
    upper = math.isqrt(d) + 1
    lowersquare = pow(lower, 2)
    uppersquare = pow(upper, 2)
    return abs(min(d - lowersquare, d - isqrsqr, uppersquare - d))
     
    

# write the function isPrefix
def isPrefix(s1, s2):
    if s2[0:len(s1)] == s1:
        return True
    elif s1[0:len(s2)] == s2:
        return True
    else:
        return False
# write the function fromTotalSeconds
def fromTotalSeconds(time):
    hourdiv = time // 3600
    hourremain = time % 3600
    minutediv = hourremain // 60
    minuteremain = hourremain % 60
    return([minuteremain, minutediv, hourdiv])
    
    



        
