#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# from decimal import *
#
#
# x = 7
# print('x is {}'.format(x))
# print(type(x))
#
# # Floating numbers are not good to make operations with money
# a = Decimal('0.10')
# b = Decimal('0.30')
# x = a + a + a - b
# print('x is {}'.format(x))
# print(type(x))
#
# # Bool type
# # x = True
# # x = None
# x = ""
# print('x is {}'.format(x))
# print(type(x))
#
# if x:
#     print('True')
# else:
#     print('False')

# type() and id()
# x = (1, 2, 3, 4, 5)
x = (1, 'two', 3.0, [4, 'four'], 5)
y = (1, 'two', 3.0, [4, 'four'], 5)
print('x is {}'.format(x))
print(type(x))
print(type(x[1]))

# identifers are different for each object
print(id(x))
print(id(y))

# though each element are the same
if x[0] is y[0]:
    print('yei')
else:
    print('nope')

# check if it is tuple
if isinstance(x, tuple):
    print('yei')
else:
    print('nope')