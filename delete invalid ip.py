import os 
import sys
import string
import re


location='c:\\'
indata=open(location,'r')

outdata=open(location.strip('.txt')+'delete invalid data.txt','a+')

pattern_ip=re.compile('\d+.\d+.\d+.\d+')
pattern=re.compile('.+\\n')

for line in indata:
	if re.match(pattern_ip,line):

a



