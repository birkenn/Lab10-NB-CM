#CREATED BY NOAH BIRKEN and CHRISOPHER MEZA
import math
def add(a, b): 
    return a+b
def subtract(a, b):
    return a-b
def multiply(a, b):
    return a*b
def divide(a, b):
    try:
        return b/a
    except ZeroDivisionError as error:
        print(str(error))
def logarithm(a,b):
    return math.log(b,a)
def exponent(a,b):
    return a**b
