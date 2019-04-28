#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

s = 'This is a long string with a bunch of words in it.'
print(s)

# split like list
print(s.split())
# results
# ['This', 'is', 'a', 'long', 'string', 'with', 'a', 'bunch', 'of', 'words', 'in', 'it.']

# same results if the format is like this
s = ''' This is a long     string with a bunch of words in it.
'''
print(s.split())

# split on specific letter, removes the i and splits it
print(s.split('i'))

# reverse the process
s = 'This is a long string with a bunch of words in it.'
l = s.split()
s2 = ' '.join(l)
print(s2)
