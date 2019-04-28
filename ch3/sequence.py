#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

## list
# x = [1, 2, 3, 4, 5]
# x[3] = 42
# for i in x:
#     print('i is {}'.format(i))

## tuple
# x = (1, 2, 3, 4, 5)
# # x[3] = 42 -> tuples are inmutable
# for i in x:
#     print('i is {}'.format(i))

## Range is inmutable unless is converted to a list
# x = range(5)
# x = range(5, 10)
# x = range(5, 50, 5)
# x = list(range(5))
# x[3] = 40
# for i in x:
#     print('i is {}'.format(i))

## dictionary
x = {'one': 1, 'two': 2, 'three': 3}

# for i in x:
#     print('i is {}'.format(i))

for k, v in x.items():
    print('key: {} and value:{}'.format(k, v))

## from chapter 13
# create the tuple
# enumarate give an index and the value
x = ('cat', 'dog')
for i, v in enumerate(x):
    print(f'{i}: {v}')