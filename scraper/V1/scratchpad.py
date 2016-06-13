import os,sys,time,math,urllib.request,urllib.parse,re

import pluginScript


spam = ['cat', 'dog', 'bat', 'anteater']
spam.sort()
print(spam)


for s in spam:
    print(s) 


spam = open('links.out', 'r')

for s in spam:
    print(s) 
