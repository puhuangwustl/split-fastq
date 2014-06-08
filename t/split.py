#!/usr/bin/python

import sys

f=open(sys.argv[1])
f1=open(sys.argv[1]+'_1.fq','w')
f2=open(sys.argv[1]+'_2.fq','w')

i=-1
for l in f:
	i+=1
	if (i/4)%2:
		f2.write(l)
	else:
		f1.write(l)

