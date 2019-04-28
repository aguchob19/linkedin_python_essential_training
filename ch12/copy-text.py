#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


# def main():
#     infile = open('lines.txt', 'rt')
#     outfile = open('lines-copy.txt', 'wt')
#     for line in infile:
#         print(line.rstrip(), file=outfile) # write the lines in the new file
#         print('.', end='', flush=True) # end prevent to print a new line after the dot
#     outfile.close()
#     print('\ndone.')
#
#
# if __name__ == '__main__': main()

# optionally the method write lines
# though the function rstrip has advantages of not having the white spaces
def main():
    infile = open('lines.txt', 'rt')
    outfile = open('lines-copy.txt', 'wt')
    for line in infile:
        outfile.writelines(line)
        print('.', end='', flush=True) # end prevent to print a new line after the dot
    outfile.close()
    print('\ndone.')


if __name__ == '__main__': main()