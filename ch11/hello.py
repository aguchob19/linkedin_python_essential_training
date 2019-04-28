#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# Common String Methods
print('Hello, World.')
print('Hello, World.'.upper())
print('Hello, World.'.capitalize())
print('Hello, World.'.title())
print('Hello, World.'.casefold()) # all even german letter

s1 = 'Hello Word'
s2 = s1.upper()

print(id(s1))
print(id(s2)) # creates a complete new object

# concatenate
s1 = 'Hello Word'
s2 = 'this is other string'
print(s1 + ' ' + s2)

# Formatting Strings
x = 42
y = 73
print('the number is {} {}'.format(x, y)) # spaces between bracelets counts
print('the number is {xx} {bb}'.format(xx=x, bb=y)) # spaces between bracelets counts
print('the number is {1} {0}'.format(x, y)) # spaces between bracelets counts
print('the number is {1} {0} {0}'.format(x, y)) # spaces between bracelets counts

# formatting instructions
print('the number is {0:<5} {1:>5}'.format(x, y)) # gives spaces between the strings
# adding leading zero
print('the number is {0:<5} {1:>05}'.format(x, y))
# adding a sign
print('the number is {0:<5} {1:>+05}'.format(x, y))

x = 42 * 747
# having a comma separation
print('the number is {:,}'.format(x))

# changing comma with point
print('the number is {:,}'.format(x).replace(',', '.'))

x = 42 * 747 * 1000
# fix number of places
print('the number is {:.3f}'.format(x).replace(',', '.'))

x = 42
# change to binary
print('the number is {:b}'.format(x))

# from python 3.6
print(f'the number is {x}')
# formatting ex.
print(f'the number is {x:.3f}')





