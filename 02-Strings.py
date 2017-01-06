#!/usr/bin/env python

import sys

def string_test():
    raw = r'this\t\n and that'
    normal = 'this\t\n and that'

    print 'raw:'
    print raw
    print ""

    print 'normal:'
    print normal
    print ""

    text = ("%d little pigs come out or I'll %s and %s and %s" % 
            (3, 'huff', 'puff', 'blow down'))
    print "text:"
    print text
    print ""

    ustring = u'A unicode \u018e string \xf1'
    print "ustring:"
    print ustring
    print ""    

    s = ustring.encode('utf-8')
    print "s:"
    print s
    print ""

    t = unicode(s, 'utf-8')
    print 't==ustring:',t==ustring


if __name__ == '__main__':
    string_test()