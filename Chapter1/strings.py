'''
This file contains string related methods.
'''

from cgitb import reset


def greetWorld():
    '''Simply prints Hello World! to the console'''
    print("Hello World!")

def greetName(name):
    '''This functions returns Hello along with the provided name.
    It makes use of concatinating strings using the '+' operator.'''
    result = "Hello " + name + "!"
    return result

def greetName2(name):
    '''This functions returns Hello along with the provided name.
    It makes use of concatinating strings using f strings.'''
    result = f"Hello {name}!"
    return result

def upperCase(text):
    '''Takes a string and returns the upper case of it.'''
    result = text.upper()
    return result

def lowerCase(text):
    '''Takes a string and returns the lower case of it.'''
    result = text.lower()
    return result

def properCase(text):
    '''Takes a string and returns the proper case of it.'''
    result = text.title()
    return result

def sentenceCase(text):
    '''Takes a string and returns the sentence case of it.'''
    result = text.capitalize()
    return result

def specialCharacters():
    '''Returns a string that includes special characters such as a an apostrophe or a backslash that are usually treated differently in a string.'''
    result = 'This is a sample string with special characters such as \', \" and \\'
    return result

def specialText():
    '''Returns a string that includes special characters such as a new line or a tab.'''
    result = 'This is a sample string with multiple lines\nThe second line includes a tab \t as well.'
    return result

def rawText():
    '''Returns a raw string that ignores special characters such as a new line or a tab.'''
    result = r'This is a sample string with multiple lines\nThe second line includes a tab \t as well.'
    return result

def stringLiterals():
    '''Returns a string that spans multiple lines by surrounding it by triple quotes or double quotes. Adding a \\ at the start of the literal avoids having an empty line.
    Indentation in string literals do not break the Python structure and any spaces will be displayed in the console.'''
    result = '''\
First Line
Second Line
Third Line'''
    return result

def mathOperatorsWithStrings(text1, text2):
    '''Strings can be concatenated (glued together) with the + operator, and repeated with *'''
    result = 3*text1 + text2
    return result

def stringLength(text):
    '''The built-in function len() returns the length of a string'''
    result = len(text)
    return result