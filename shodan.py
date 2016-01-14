import shodan
import re
import sys
import os

SHODAN_API_KEY = "Mawfb3ne6mFteBiRLkbDH6v5UfKyizdj"
api = shodan.Shodan(SHODAN_API_KEY)

try:
 # Print general info
 host = api.host('116.226.43.134')
 print """
        IP: %s
        Organization: %s
        Operating System: %s
 """ % (host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a'))

 # Print all banners
 for item in host['data']:
        print """
                Port: %s
                Banner: %s

        """ % (item['port'], item['data'])
except shodan.APIError, e:
        print 'Error: %s' % e
    
