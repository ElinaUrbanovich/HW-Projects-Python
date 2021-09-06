def plus(a, b):
    return float(a) + float(b)

def minus(a, b):
    return float(a) - float(b)

def multiply(a, b):
    return float(a) * float(b)

def divide(a, b):
    try:
        return float(a) / float(b)
    except ZeroDivisionError:
        return 'You cannot divide by zero'

