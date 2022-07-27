# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 15:26:58 2022

@author: Alexander Aronson
"""
"""
Problem 1
    1.Define a function which have multiple parameters with one default parameter value and return multiple values.
    2.Call the function to calculate the return values for your given arguments.
    3.Call the function to calculate the return values using keyword arguments.
Problem 2
    1.Define a function with a function parameter.
    2.Call the function to calculate the return values for your given arguments.
Problem 3
    1.Create a lambda function with multiple parameters.
    2.Calculate the lambda function return value for your given arguments.
Problem 4
    1.Design a map() function using lambda function as function parameter.
    2.Call the map() function to calculate the return values for your given list.
"""
############SPACER#############################################################

'Problem 1'
'Q1 & Q2'
def add(x,y,z=3):
    return (x*y)**z
a=add(2,3)
b=add(1,9,4)
c=add(1,2,-3)
print(a,b,c)

'Q3'
add(x=2,y=3,)
add(x=1,y=9,z=4)
add(x=1,y=2,z=-3)

'Problem 2' 
'Q1 & Q2'
def my_function(a,func):
    return func(a)
import math
fact = math.factorial
b=my_function(5,fact)
print(b)

'Problem 3'
'Q1 & Q2'
w = lambda x,y,z: (x/z)**y
import math
x=math.factorial
y=math.exp
l=w(5,4,3)
print(l)

'Problem 4'
'Q1 & Q2'
import numpy as np
V1 = [32,15,76]
V2=[[12],
    [1],
    [33]]
Dot = (list(map(lambda V1,V2: np.dot(V1,V2), V1, V2)))
print(Dot)



