def IsInt(value):
    # Returns True if the value is an integer and False otherwise
    if type(value) is int:
        return True
    else:
        return False

def IsFloat(value):
    # Returns True if the value is a float and False otherwise
    if type(value) is float:
        return True
    else:
        return False

def IsString(value):
    # Returns True if the value is a string and False otherwise
    if type(value) is str:
        return True
    else:
        return False

def IsBool(value):
    # Returns True if the value is a boolean and False otherwise
    if type(value) is bool:
        return True
    else:
        return False

def ConvertToInt(a):
    # Returns a as an integer. If a is a float, it discards the float part and only return the whole part. If a is a valid int it returns it as an int, otherwise it throws an error
    return int(a)

def ConvertToFloat(a):
    # Returns a as a float. If a is an int, it adds a decimal point to it. If a is a valid float it returns it as an float, otherwise it throws an error
    return float(a)

def ConvertToString(a):
    # Returns a as a string
    return str(a)
