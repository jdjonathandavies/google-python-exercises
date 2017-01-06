#!/usr/bin/env python

import sys

def sort_test():
    a=[5,1,4,3]
    print "sorted(a): ", sorted(a)
    print "sorted(a, reverse=True): ", sorted(a,reverse=True)
    print "a: ", a

    strs = ['aa', 'BB', 'zz', 'CC']
    print "sorted(strs): ", sorted(strs)
    print "sorted(strs, reverse=True): ", sorted(strs, reverse=True)

    strs = ['ccc', 'aaaa', 'd', 'bb']
    print "sorted(strs, key=len): ", sorted(strs, key=len)  ## ['d', 'bb', 'ccc', 'aaaa']
    print "sorted(strs, key=str.lower): ", sorted(strs, key=str.lower)

    ## Say we have a list of strings we want to sort by the last letter of the string.
    strs = ['xc', 'zb', 'yd' ,'wa']
  
    ## Write a little function that takes a string, and returns its last letter.
    ## This will be the key function (takes in 1 value, returns 1 value).
    def MyFn(s):
      return s[-1]
  
    ## Now pass key=MyFn to sorted() to sort by the last letter:
    print "sorted(strs, key=MyFn): ", sorted(strs, key=MyFn) 

def tuple_test():
    tupley = (1,2,'hi')
    print "tupley: ", tupley
    print "len(tupley): ", len(tupley)
    print "tupley[2]: ", tupley[2]
#    tupley[2] = 'bye'
    tupley = ('hi',)
    print "tupley: ", tupley

    (x, y, z) = (42, 13, "hike")
    print "x:",x,"y:",y,"z:",z

def list_comprehensions_test():

    nums = [1,2,3,4]
    squares = [ n*n for n in nums ]
    print "nums:", nums
    print "squares:", squares

    strs = ['hello','and','goodbye']
    shouting = [ s.upper() + '!!!' for s in strs]
    print "strs:", strs
    print "shouting:", shouting

    nums = [2,8,1,6]
    small = [ n for n in nums if n <=2 ]
    print "nums:", nums
    print "small:", small

    fruits = ['apple', 'cherry', 'bannana', 'lemon']
    afruits = [s.upper() for s in fruits if 'a' in s]
    print "fruits:", fruits
    print "afruits:", afruits



if __name__ == '__main__':
    sort_test()
    tuple_test()
    list_comprehensions_test()