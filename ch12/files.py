#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


# def main():
#     f = open('lines.txt')
#     for line in f:
#         print(line.rstrip()) #rstrip strip the white spaces in the end of the line
#
# if __name__ == '__main__':
#     main()

# uper is the same as:
# def main():
#     f = open('lines.txt', 'r') # can be 'w', starts in the beginning and if the file does not exist it creates it
#     for line in f:
#         print(line.rstrip()) #rstrip strip the white spaces in the end of the line
#
#
# if __name__ == '__main__':
#     main()

# write
# def main():
#     f = open('lines.txt', 'w') # can be 'w', empty the file and if the file does not exist it creates it
#     for line in f:
#         print(line.rstrip()) #rstrip strip the white spaces in the end of the line
#
#
# if __name__ == '__main__':
#     main()


# if the file exists, use append and starts in the end, does not empty the file
# def main():
#     f = open('lines.txt', 'a')
#     for line in f:
#         print(line.rstrip()) #rstrip strip the white spaces in the end of the line
#
#
# if __name__ == '__main__':
#     main()

# text or binary incluses +t or +b; default is text format
def main():
    f = open('lines.txt', 'w+t') # or r+b or r+a
    for line in f:
        print(line.rstrip()) #rstrip strip the white spaces in the end of the line


if __name__ == '__main__':
    main()
