import re
import os
import sys
import string
import subprocess
import urllib2

leixing=['CA-HZ1020S','CA-HZ2012S','CVR','DH-DVR2108C-W-SK','DH-IPC-HDW3150P','DH-IPC-HF8291E',
'DH-IPC-HFW2100B-V2',
'DH-IPC-HFW3108D',
'DH-IPC-HFW4305B-V2',
'DH-IPC-HFW7105N',
'DH-NVR7816',
'DH-NVR7832',
'DH-NVS0404HG-AS-E',
'DH-SD-42D212S-HN',
'DH-SD-59D120S-GN',
'DH-SD-59D220S-GN',
'DH-SD-59D220S-HN',
'DH-SD6582A-HN',
'DH-SD6582A-HNAG',
'DH-SD-65A120-HN',
'DH-SD-65D120S-HN',
'DH-SD-65D220S-HN',
'DH-SD69118B-HN',
'DH-SD6980C-HN',
'DH-SD6980C-HN-DC',
'DH-SD6980-HN',
'DH-SD6982A-HN',
'DH-SD6982C-HN',
'DH-SD6982-HN',
'DH-SD-6A1120-HN',
'DH-SD-6A1120S-HN',
'DH-SD-6A120S-HN',
'DH-SD-6A1220-HNI',
'DH-SD-6A1220-S',
'DH-SD-6A1220S-HN',
'DH-SD-6A2230X-HNI',
'DH-SD6A83A-HN',
'DH-SD-6C1120S-GN',
'DH-SD-6C1120S-HN',
'DH-SD-6C1220S-HN',
'DH-SD-6C1230S-HN',
'DH-SD-6C2230X-HNI',
'DH-SD6C80B-GN',
'DH-SD6C80D-GN',
'DM368',
'DVR',
'HCVR',
'HDB3200',
'HDVR',
'ipc',
'IP_Camera',
'IPC-F728WP',
'IPC-HD2100',
'IPC-HD3100',
'IPC-HDB3100C',
'IPC-HDB4150F-PT',
'IPC-HDBW3110',
'IPC-HDBW3300',
'IPC-HDBW4250E-AS',
'IPC-HDBW5101R',
'IPC-HDW1100S',
'IPC-HDW1105S',
'IPC-HDW2100',
'IPC-HDW2100S-V2',
'IPC-HDW2105',
'IPC-HDW2105S-V2',
'IPC-HDW2125S',
'IPC-HDW2200S-V2',
'IPC-HDW2205S-V2',
'IPC-HDW3100',
'IPC-HDW3100S',
'IPC-HDW3105S',
'IPC-HDW3105S-V2',
'IPC-HDW3200',
'IPC-HDW3300S',
'IPC-HDW4100C',
'IPC-HDW4100S-V2',
'IPC-HDW4105C',
'IPC-HDW4105S',
'IPC-HDW4105S-V2',
'IPC-HDW4300C',
'IPC-HDW4300S',
'IPC-HDW4300S-V2',
'IPC-HDW4305C',
'IPC-HDW4305S-V2',
'IPC-HF3100',
'IPC-HF3101',
'IPC-HF3200',
'IPC-HF3300',
'IPC-HF5100',
'IPC-HF5200',
'IPC-HF5210-I',
'IPC-HF8291E',
'IPC-HFW1025D',
'IPC-HFW1100B',
'IPC-HFW1105B',
'IPC-HFW1105S',
'IPC-HFW2100',
'IPC-HFW2100B-V2',
'IPC-HFW2100D',
'IPC-HFW2100D-V2',
'IPC-HFW2105B',
'IPC-HFW2105B-V2',
'IPC-HFW2105D-V2',
'IPC-HFW2105S',
'IPC-HFW2125B',
'IPC-HFW2200D',
'IPC-HFW2200S',
'IPC-HFW2200S-V2',
'IPC-HFW2205B-V2',
'IPC-HFW3100',
'IPC-HFW3100C',
'IPC-HFW3100D',
'IPC-HFW3100P-V2',
'IPC-HFW3105',
'IPC-HFW3105P-V2',
'IPC-HFW3200C',
'IPC-HFW3200D',
'IPC-HFW3200S',
'IPC-HFW3300',
'IPC-HFW3300C',
'IPC-HFW4100B',
'IPC-HFW4100B-V2',
'IPC-HFW4100D-AS',
'IPC-HFW4105B',
'IPC-HFW4105B-AS',
'IPC-HFW4105B-V2',
'IPC-HFW4105D',
'IPC-HFW4120B',
'IPC-HFW4150B-V2',
'IPC-HFW4200D',
'IPC-HFW4205B',
'IPC-HFW4205D',
'IPC-HFW4300D-V2',
'IPC-HFW4305B',
'IPC-HFW4305B-V2',
'IPC-HFW4305D',
'IPC-HFW4305D-AS',
'IPC-HFW4305D-V2',
'IPC-HFW4350D-V2',
'IPC-HFW5100C',
'IPC-HFW5100C-L',
'IPC-HFW5100D',
'IPC-HFW5150R-VF',
'IPC-HFW5200C',
'IPC-HFW5200D',
'IPC-HFW5200-IRA',
'IPC-HFW5200-IRA-L',
'IPC-HFW5250C',
'IPC-HFW5250R-Z',
'IPC-HFW8351E',
'IPC-HW1306',
'IPC-K100A',
'IPC-K100W',
'IPC-KW12W',
'IPC-KW12W-CE',
'IP_PTZ_Dome',
'ITC102-GVRB3A',
'ITC213-GVRB3B-H',
'ITC302-GVRB3A',
'NVR',
'NVR6000',
'NVS',
'SD',
'SD65XX-HN',
'SD6AXX-HN',
'SD6C80D-HN',
'SD6XXX-HN',
'test',
'VS-DHSD-6A1120SHN',]
class MyException(Exception):
    pass

port=[80,81,82,8000,8888,8081,9000]
location='c:\\1.txt'

pattern_ip=re.compile('\d+.\d+.\d+.\d+')
pattern_num=re.compile('\d+/')
pattern_rtsp1='Server: Rtsp'
pattern_rtsp2='WWW-Auth'
pattern_http='SERVER:'

indata=open(location,'r')
outdata=open(location.strip('.txt')+'-output.txt','a+')

for line in indata:
    if line.strip('\n') in leixing:
        outdata.write(line)
        continue
    elif re.match(pattern_ip,line):
        ip=re.match(pattern_ip,line).group()
    elif re.match(pattern_num,line):
        port_num=re.match(pattern_num,line).group().strip('/')
        if int(port_num) in port:
          print 'http://'+str(ip)+':'+port_num
          try:
            response=urllib2.urlopen('http://'+str(ip)+':'+port_num,timeout=15)
            length=len(response.read())
            htmlout=open('C:\\Users\\lzh\\Desktop\\html\\brand+'--'+str(ip)+'-'+str(p)+'.txt'','a+')
            htmlout.write(response.read())
            htmlout.close()
            outdata.write('http-length:'+str(length)+'\n')
          except urllib2.URLError,e:
             print  e
        else:
          continue
    elif re.match(pattern_rtsp1,line):
        outdata.write(line+'\n')
    elif re.match(pattern_rtsp2,line):
        outdata.write(line+'\n')
    elif re.match(pattern_http,line):
        outdata.write(line+'\n')
    else:
        continue
indata.close()
outdata.close()
