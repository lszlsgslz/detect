#coding:utf-8
#对摄像头进行分类
import sys
import os

in_json=open("c:\\Dahua-json.txt",'r')
in_leixing=open("c:\\leixing.txt",'r')
out=open('C:\\Users\\zhongxin\\Desktop\\out.txt','w')
lines=in_json.readlines()

for line in in_leixing.readlines():
    line=line.strip('\n')
    out.write(line)
    out.write('\n')
    for line1 in lines:        
        a=(line1.split(',')[7])
        if str(line)==str(a):
            print ('-----------------')
            out.write(line1)
            
out.close()
in_json.close()
in_leixing.close()
