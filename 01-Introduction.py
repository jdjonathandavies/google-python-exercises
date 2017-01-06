#!/usr/bin/env python

import sys

def repeat(s,exclaim):
    result = s + ' ' + s + ' ' + s
    if exclaim:
        result = result + '!!!'
    return result

def main():
    print "The number of arguments is: %i" %(len(sys.argv))
    for i,arg in enumerate(sys.argv):
        print "Argument %i: %s" %(i,arg)
    print "Hello there", sys.argv[1]
    print repeat(sys.argv[1], True)

if __name__ == '__main__':
    main()