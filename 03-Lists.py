#!/usr/bin/env python

import sys

def list_test():
    colors = ['red','blue','green']
    print "len(colors): ", len(colors)
    print "colors[2]: ", colors[2]
    print "colors[0]: ", colors[0]
    b = colors
    print "b: ", b
    b[0]=b[1]
    print "colors: ", colors

    squares = [1,4,9,16]
    sum = 0
    for num in squares:
        sum += num
        print "num: %d sum: %d" %(num, sum)

    print "sum: %d" % sum

    names = ['larry', 'curly', 'moe']
    if 'curly' in names:
        print 'curly: %s' % 'yay'

    print "names: ", names
    print "names.index('curly'): ", names.index('curly')

    names.append('shemp')
    names.insert(0, 'xxx')
    names.extend(['yyy', 'zzz'])

    print "names: ", names
    print "names.index('curly'): ", names.index('curly')

    names.remove('curly')
    print "names.pop(1): ", names.pop(1)
    print "names: ", names

    names = []          ## Start as the empty list
    names.append('a')   ## Use append() to add elements
    names.append('b')

    




def range_test():
    for i in range(10):
        print "i %d" % i

def while_test(a):
    i = 0
    while i < len(a):
        print a[i]
        i = i+3

if __name__ == '__main__':
    list_test()
#    range_test()
#    while_test([x for x in range(100)])