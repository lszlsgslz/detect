import sys
import os
import re
import string

pattern=re.compile('DS-.+')
in_json=open("c:\\Hikvision\\every10ip.txt",'r')
out=open(r'c:\\Hikvision\\10ip--out.txt','w')
lines=in_json.readlines()

for line in lines:
 if re.match(pattern,line):
    out.write(line)
    n=0
    continue
 else:
    if n<10:
      out.write(line)
      n+=1
    else:
      continue
	    
out.close()
in_json.close()
