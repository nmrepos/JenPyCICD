#!/usr/bin/env python

'''
A simple command line tool that takes 2 values and adds them together using
the calc.py library's 'add2' function.
'''

import sys
import calc

def convert_to_number_if_possible(inputString):
    '''
    Attempts to convert the given string to a number (int or float).
    If conversion is not possible, returns the original string.
    '''
    try:
        return int(inputString)
    except ValueError:
        try:
            return float(inputString)
        except ValueError:
            return inputString

def main():
    '''
    This main method prompts the user for 2 values and outputs the result
    of adding them together.
    '''
    print('This tool takes 2 values and adds them together.')
    
    # Get first value
    input1 = input("Enter first value: ")
    if input1 == '':
        print("You must enter a value.")
        return 1
    
    # Get second value  
    input2 = input("Enter second value: ")
    if input2 == '':
        print("You must enter a value.")
        return 1
    
    # Convert inputs to numbers if possible
    val1 = convert_to_number_if_possible(input1)
    val2 = convert_to_number_if_possible(input2)
    
    # Add the values
    result = calc.add2(val1, val2)
    
    # Display result
    print(f"The result is: {result}")
    return 0

if __name__ == '__main__':
    sys.exit(main())
