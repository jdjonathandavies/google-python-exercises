#!/usr/bin/env python

import sys
import re

def test_re_1():
    text = 'an example word:cat!!'
    match = re.search(r'word:\w\w\w',text)
    print 'text:',text
    if match:
        print 'found', match.group()
    else:
        print 'did not find anything'

    ## Search for pattern 'iii' in string 'piiig'.
    ## All of the pattern must match, but it may appear anywhere.
    ## On success, match.group() is matched text.


def test_re(pattern,text):
    match = re.search(pattern,text)
    print "%-40s => " % ("re.search(r'%s','%s')" % (pattern, text)),

    if match:
        print match.group()
    else:
        print ""
    return match

def get_email(text):
#    return test_re(r'\w+@\w+', text)
    match = test_re(r'([\w,-]+)@([\w.-]+)', text)
    if match:
        print "username:", match.group(1)
        print "host:", match.group(2)

def test_findall(pattern, text):

    print "%-40s => " % ("re.findall(r'%s','%s')" % (pattern, text)),
    matches = re.findall(pattern,text)
    for match in matches:
        print match,
    print ""
    return matches

def test_sub(pattern, replacement, text):
    print "%-50s" % ('re.sub(r"%s",r"%s","...")' % (pattern,replacement))
    print "'%s' => '%s'" % (text, re.sub(pattern,replacement,text))



if __name__ == '__main__':
#    test_re_1()
    test_re(r'iii', 'piiig')
    test_re(r'igs', 'piiig')
    test_re(r'..g', 'piiig')
    test_re(r'\d\d\d', 'p123g')
    test_re(r'\w\w\w', '@@abcd!!')
    test_re(r'pi+', 'piiig')
    test_re(r'i+', 'piigiiii')                    
    test_re(r'\d\s*\d\s*\d', 'xx1 2   3xx')
    test_re(r'\d\s*\d\s*\d', 'xx12  3xx')
    test_re(r'\d\s*\d\s*\d', 'xx123xx')
    test_re(r'^b\w+', 'foobar')
    test_re(r'b\w+', 'foobar')

    get_email('purple alice-b@googlemail.com monkey dishwasher')
    test_findall(r'([\w\.-]+)@([\w\.-]+)', 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher')
    test_sub(r'([\w\.-]+)@([\w\.-]+)', r'\1@mofo.com', 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher')
