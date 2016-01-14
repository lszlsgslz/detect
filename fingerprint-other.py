import os
import shodan
import re
import sys
import subprocess

SHODAN_API_KEY = "Mawfb3ne6mFteBiRLkbDH6v5UfKyizdj"
api = shodan.Shodan(SHODAN_API_KEY)
location='c:\\down-output.txt'


pattern_ip=re.compile('\d+.\d+.\d+.\d+')
pattern_port=re.compile('\d+/tcp\s+open\s+\w+')
pattern_num=re.compile('\d{1,5}')
pattern_md5=re.compile('\w{32}')
indata=open(location,'r')

for line in indata:

  outdata=open(location.strip('.txt')+'-other-output.txt','a+')
  outdata.write(line)

  if re.match(pattern_port,line):
    port=re.match(pattern_num,line)
    data=''
    if port=='23':

    elif port=='80'or'81'or'82'or'8080'or'8000':
      tmp_data=subprocess.Popen('nmap '+'-p '+str(port)+' --script http-favicon.nse '+str(ip), shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
      nmap_data=re.findall(tmp_data.stdout.read())
      outdata.write(nmap_data+'\n')

      

    outdata.write(line.strip('\n'))
    ip=re.match(pattern_ip,line).group()
    print ip
    #nmap_data=os.popen('nmap '+str(ip)).read()
    print 'nmaping~~~~~~~~~~~~'
    nmap_data= subprocess.Popen('nmap '+str(ip), shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    nmap_port=re.findall(pattern_port,nmap_data.stdout.read())
    tmp='\n'
    outdata.write(tmp)
    
    line=line.strip('\n')
    for port_line in nmap_port:
        tmp+=port_line+'\n'
        print port_line
    try:
        print 'shodaning~~~~~~~~~~~~'
        host=api.host(ip)
        org=host.get('org','n/a')
        os=host.get('os', 'n/a')
        port=host.get('port','n/a')       
        tmp=tmp.strip('\n')
        for service in host['data']:
          tmp=tmp+'Port:'+str(service['port'])+'\n'+'Banner:'+str(service['data'])
        outdata.write(org+','+str(os)+','+str(port)+','+'\n'+tmp+'\n')
        
    except shodan.APIError, e:
        print 'Error: %s' % e   
    
  else:
      outdata.write(line)
      continue
    
  outdata.close()

indata.close()
