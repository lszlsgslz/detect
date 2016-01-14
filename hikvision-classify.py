#coding:utf-8
#hikvision处理
import sys
import os
import re
import string
location="c:\\Hikvision\\"
in_leixing=open("c:\\Hikvision\\leixing.txt",'r')
out=open('C:\\Hikvision\\Hikvision-out.txt','w')

m=0
for line in in_leixing:
    a=1
    line=line.strip('\n')
    out.write(line)
    out.write('\n')
    for i in range(8):       
      in_json=open(location+str(a)+'.txt','r')
      lines=in_json.readlines()
      a+=1
      for line1 in lines:
        c=line1.split(',')
        if len(c)>7:    
           b=c[7]
        else:
            m=m+1
            continue
        if str(line)==str(b):
            print ('-----------------')
            out.write(line1)
      in_json.close()
            
out.close()
in_leixing.close()
print '!!!!!!!!!!!!'
print m
