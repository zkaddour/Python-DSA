'''
This file contains mathematical classes and functions. Some of them are as basic as adding two numbers together, while others will handle vectors or complex numbers.
'''

def additionSimple(a,b):
    '''Returns the sum of a and b'''
    result = a + b
    return result

def substractionSimple(a,b):
    '''Substracts b from a'''
    result = a - b
    return result

def multiplicationSimple(a,b):
    '''Multiplies a times b'''
    result = a * b
    return result

def divisionSimple(a,b):
    '''Divides a by b, if b equals 0 it returns an infinite number'''
    if b == 0:
        return float('inf')
    result = a / b
    return result

def squarred(a):
    '''Returns the squarred value of a'''
    result = a ** 2
    return result

def powerOf(a,b):
    '''Returns a to the power of b'''
    result = a ** b
    return result

def modulus(a,b):
    '''Returns the remainder of the devision of a by b, if b equals 0 it returns an infinite number'''
    if b == 0:
        return float('inf')
    result = a % b
    return result

def divisionFloor(a,b):
    '''Divides a by b and discards the fractional part, if b equals 0 it returns an infinite number'''
    if b == 0:
        return float('inf')
    result = a // b
    return result