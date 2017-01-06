#!/usr/bin/env python

import sys
import codecs

def dict_test():
    dicty = {}
    dicty['a'] = 'alpha'
    dicty['g'] = 'gamma'
    dicty['o'] = 'omega'
    print "dicty:",dicty

    print "dicty['a']:",dicty['a']
    dicty['a']=6
    print "'a' in dicty:", 'a' in dicty
    if 'z' in dicty: print dicty['z']
    print "dicty.get('z'):",dicty.get('z')

    for key in dicty: print key
    for key in dicty.keys(): print key
    print "dicty.keys():", dicty.keys()
    print "dicty.values():", dicty.values()

    for key in sorted(dicty.keys()): print "key:", key, "value:", dicty[key]

    print "dicty.items():", dicty.items()

    for key,value in dicty.items(): print key,">",value

def dict_detail_test():
    hashy = {}
    hashy['word'] = 'garfield'
    hashy['count'] = 42
    s = 'I want %(count)d copies of %(word)s' % hashy
    print s

    var = 6
    del var
    listy = ['a','b','c','d']
    print 'listy:',listy
    del listy[0]
    del listy[-2]
    print "listy:",listy

    dicty = {'a':1, 'b':2, 'c':3}
    print 'dicty:',dicty
    del dicty['b']
    print 'dicty:',dicty

def file_test():
    f = open('basic/small.txt','rU')
    for line in f:
        print line,
    f.close()


if __name__ == '__main__':
    dict_test()
    dict_detail_test()
    file_test()