#!/usr/bin/env python

import string

f=open('twl.txt','r')
dict=f.readlines()

for i in string.lowercase:
    for j in string.lowercase:
        str='{0}{1}'.format(i,j)
        count=0
        for k in dict:
            if str in k:
	        count += 1
        print '{0}{1} - {2}'.format(i,j,count)
