'''
A library that provides a simple addition function.
'''

def add2(arg1, arg2):
    '''
    Summary line.

    Extended description of function.

    Parameters:
    arg1 : int or str
        Description of arg1
    arg2 : int or str
        Description of arg2

    Returns:
    int or str
        Description of return value

    '''
    # If either argument is a string, convert both to strings for concatenation
    if isinstance(arg1, str) or isinstance(arg2, str):
        return str(arg1) + str(arg2)
    
    # Otherwise, perform numeric addition
    return arg1 + arg2

def subtract2(arg1, arg2):
    '''
    Summary line.

    Extended description of function.

    Parameters:
    arg1 : int
        Description of arg1
    arg2 : int
        Description of arg2

    Returns:
    int
        Description of return value

    '''

    return arg1 - arg2
